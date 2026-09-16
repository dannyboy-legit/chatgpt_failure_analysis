import unittest
from controller import (
    Constraint, Controller, ControllerError, EditContract, QAResult,
    ReferenceRole, Status, Verdict, susan_reference_roles,
)


def c(cid, value, source="Susan_v5", rank=100, scope="identity", **kw):
    return Constraint(cid, value, source, "canonical", rank, scope,
                      observable_predicate=f"observe:{cid}", **kw)


class ControllerTests(unittest.TestCase):
    def setUp(self):
        self.ctrl = Controller()
        for r in susan_reference_roles("face_profile", "physique_side"):
            self.ctrl.add_reference(r)
        self.ctrl.add_constraint(c("SUSAN_FACE_IDENTITY", "canonical", scope="identity"))
        self.ctrl.add_constraint(c("SUSAN_PHYSIQUE", "canonical", scope="physique"))
        self.ctrl.add_constraint(c("CAMERA_LOCK", "base_camera", source="accepted_base", rank=90, scope="camera"))

    def test_stale_source_cannot_override_canon(self):
        with self.assertRaisesRegex(ControllerError, "AUTHORITY_REBINDING"):
            self.ctrl.add_constraint(c("SUSAN_FACE_IDENTITY", "old_chloe", source="old_addendum", rank=20))

    def test_generated_descendant_cannot_rebind_identity(self):
        with self.assertRaisesRegex(ControllerError, "AUTHORITY_REBINDING"):
            self.ctrl.add_constraint(c("SUSAN_FACE_IDENTITY", "artifact_17_face", source="artifact_17", rank=10))

    def test_pose_reference_cannot_donate_identity(self):
        self.ctrl.add_reference(ReferenceRole("pose_other_woman", "pose", ("pose",),
                                              ("facial_geometry", "anatomy", "silhouette"), 40, False))
        self.assertNotIn("facial_geometry", self.ctrl.state.references["pose_other_woman"].allowed)

    def test_canonical_reference_scene_leak_rejected(self):
        bad = Controller()
        bad.add_reference(ReferenceRole("bad_face", "canonical_face", ("facial_geometry", "pose"), (), 100, True))
        with self.assertRaisesRegex(ControllerError, "REFERENCE_CONTAMINATION_RISK"):
            bad.validate_reference_roles()

    def test_missing_reference_fails_closed(self):
        with self.assertRaisesRegex(ControllerError, "MISSING_REFERENCE"):
            self.ctrl.precommit_audit(EditContract(), ["face_profile", "physique_side", "missing_pixels"])

    def test_edit_contract_conflict_rejected(self):
        contract = EditContract(must_change={"left_leg"}, must_not_change={"left_leg"})
        with self.assertRaisesRegex(ControllerError, "EDIT_CONTRACT_CONFLICT"):
            self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])

    def test_failed_route_cannot_repeat(self):
        contract = EditContract(must_change={"scale"}, must_not_change={"camera"})
        fp = self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])
        self.ctrl.reject(fp, "wrong identity")
        with self.assertRaisesRegex(ControllerError, "REJECTED_ROUTE_REUSE"):
            self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])

    def test_unverifiable_is_not_pass(self):
        qa = QAResult({"SUSAN_FACE_IDENTITY": Verdict.UNVERIFIABLE, "CAMERA_LOCK": Verdict.PASS})
        self.assertFalse(self.ctrl.verify_artifact(qa, ["SUSAN_FACE_IDENTITY", "CAMERA_LOCK"]))

    def test_transaction_rolls_back_on_hard_failure(self):
        contract = EditContract(must_change={"scale"}, must_not_change={"camera"})
        fp = self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])
        qa = QAResult({"SUSAN_FACE_IDENTITY": Verdict.PASS, "CAMERA_LOCK": Verdict.FAIL})
        with self.assertRaisesRegex(ControllerError, "TRANSACTION_ABORTED"):
            self.ctrl.commit("bad_artifact", fp, qa, ["SUSAN_FACE_IDENTITY", "CAMERA_LOCK"])
        self.assertIsNone(self.ctrl.state.current_edit_base)
        self.assertIn(fp, self.ctrl.state.rejected_fingerprints)

    def test_successful_transaction_commits(self):
        contract = EditContract(must_change={"scale"}, must_not_change={"camera"})
        fp = self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])
        qa = QAResult({"SUSAN_FACE_IDENTITY": Verdict.PASS, "CAMERA_LOCK": Verdict.PASS})
        self.ctrl.commit("good_artifact", fp, qa, ["SUSAN_FACE_IDENTITY", "CAMERA_LOCK"])
        self.assertEqual(self.ctrl.state.current_edit_base, "good_artifact")

    def test_historical_state_excluded_from_packet(self):
        self.ctrl.add_constraint(Constraint("OLD_POSE", "x", "old_turn", "history", 1, "pose",
                                           observable_predicate="observe:old", status=Status.HISTORICAL))
        self.assertNotIn("OLD_POSE", {x.constraint_id for x in self.ctrl.normalize()})

    def test_cousin_prompt_equivalence_at_ir_level(self):
        # Natural-language parsing is intentionally outside this deterministic prototype.
        # Once two phrasings resolve to the same constraints, packet fingerprints must match.
        contract = EditContract(must_change={"scale"}, must_not_change={"camera"})
        fp1 = self.ctrl.precommit_audit(contract, ["face_profile", "physique_side"])
        fp2 = self.ctrl.precommit_audit(contract, ["physique_side", "face_profile"])
        self.assertEqual(fp1, fp2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
