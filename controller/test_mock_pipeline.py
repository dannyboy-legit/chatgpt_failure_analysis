import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from controller import Constraint, Controller, ControllerError, EditContract, QAResult, Verdict
from mock_pipeline import MockImageExecutor, SusanReferenceManifest, run_mock_pipeline


FACE = b"deterministic-susan-face-fixture-v5"
PHYS = b"deterministic-susan-physique-fixture-v5"


def h(b): return hashlib.sha256(b).hexdigest()


def build_fixture(root: Path):
    (root / "refs").mkdir()
    (root / "refs/face.bin").write_bytes(FACE)
    (root / "refs/phys.bin").write_bytes(PHYS)
    manifest = {
        "references": [
            {"reference_id":"FACE","path":"refs/face.bin","sha256":h(FACE),"source_class":"canonical_face",
             "allowed":["facial_geometry"],"forbidden":["pose","physique","wardrobe","environment","expression","lighting","camera"],
             "authority_rank":100,"canonical":True,"view":"front","version":"v5"},
            {"reference_id":"PHYS","path":"refs/phys.bin","sha256":h(PHYS),"source_class":"canonical_physique",
             "allowed":["anatomy","silhouette"],"forbidden":["facial_geometry","pose","wardrobe","environment","expression","lighting","camera"],
             "authority_rank":100,"canonical":True,"view":"front","version":"v5"}
        ]}
    p = root / "manifest.json"; p.write_text(json.dumps(manifest))
    return SusanReferenceManifest.load(p)


def controller():
    c = Controller()
    c.add_constraint(Constraint("identity", "Susan v5", "SusanBibleV5", "canonical_doc", 100,
                                "identity", True, "face matches canonical Susan geometry"))
    c.add_constraint(Constraint("physique", "canonical", "SusanBibleV5", "canonical_doc", 100,
                                "physique", True, "anatomy and silhouette match canonical physique"))
    return c


class MockPipelineTests(unittest.TestCase):
    def test_end_to_end_success_and_receipt(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); m=build_fixture(root); c=controller()
            qa=QAResult({"identity":Verdict.PASS,"physique":Verdict.PASS})
            r=run_mock_pipeline(c,m,root,["FACE","PHYS"],EditContract(must_not_change={"identity","physique"}),
                                "controlled Susan scene",qa,["identity","physique"])
            self.assertEqual(r.transmitted_reference_ids,("FACE","PHYS"))
            self.assertEqual(r.transmitted_reference_sha256["FACE"],h(FACE))
            self.assertEqual(c.state.current_edit_base,r.artifact_id)

    def test_checksum_tamper_fails_before_execution(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); m=build_fixture(root); (root/"refs/face.bin").write_bytes(b"tampered")
            with self.assertRaisesRegex(ControllerError,"REFERENCE_CHECKSUM_MISMATCH"):
                run_mock_pipeline(controller(),m,root,["FACE","PHYS"],EditContract(),"x",
                                  QAResult({"identity":Verdict.PASS}),["identity"])

    def test_transport_drop_fails_and_does_not_commit(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); m=build_fixture(root); c=controller()
            with self.assertRaisesRegex(ControllerError,"TRANSPORT_REFERENCE_MISSING"):
                run_mock_pipeline(c,m,root,["FACE","PHYS"],EditContract(),"x",
                                  QAResult({"identity":Verdict.PASS,"physique":Verdict.PASS}),
                                  ["identity","physique"],MockImageExecutor(drop_reference="FACE"))
            self.assertIsNone(c.state.current_edit_base)

    def test_qa_failure_rolls_back(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); m=build_fixture(root); c=controller()
            with self.assertRaisesRegex(ControllerError,"TRANSACTION_ABORTED"):
                run_mock_pipeline(c,m,root,["FACE","PHYS"],EditContract(),"x",
                                  QAResult({"identity":Verdict.FAIL,"physique":Verdict.PASS}),
                                  ["identity","physique"])
            self.assertIsNone(c.state.current_edit_base)
            self.assertEqual(len(c.state.rejected_fingerprints),1)

    def test_unverifiable_is_not_pass(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); m=build_fixture(root); c=controller()
            with self.assertRaisesRegex(ControllerError,"TRANSACTION_ABORTED"):
                run_mock_pipeline(c,m,root,["FACE","PHYS"],EditContract(),"x",
                                  QAResult({"identity":Verdict.UNVERIFIABLE,"physique":Verdict.PASS}),
                                  ["identity","physique"])
            self.assertIsNone(c.state.current_edit_base)

    def test_path_escape_fails(self):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d); outside=root.parent/"outside-fixture.bin"; outside.write_bytes(FACE)
            manifest={"references":[{"reference_id":"FACE","path":"../outside-fixture.bin","sha256":h(FACE),
                "source_class":"canonical_face","allowed":["facial_geometry"],"forbidden":[],"authority_rank":100,
                "canonical":True,"view":"front","version":"v5"}]}
            p=root/"m.json"; p.write_text(json.dumps(manifest)); m=SusanReferenceManifest.load(p)
            with self.assertRaisesRegex(ControllerError,"REFERENCE_PATH_ESCAPE"):
                m.resolve_payloads(root,["FACE"])
            outside.unlink(missing_ok=True)


if __name__ == "__main__": unittest.main()
