# Failure Record: Susan Wallpaper Workflow

## User intent
Create a realistic desktop wallpaper featuring the established recurring character Susan, using the canonical Susan references and project rules already available to the assistant.

## Observed failures

1. **Reference-authority neglect**
   - The assistant knew Susan was a specific recurring character but generated generic brunettes before consulting the canonical face and physique references.
   - The Susan Character Bible explicitly says the canonical face references are the primary authority for facial identity and the physique references separately govern physique/silhouette.

2. **Failure to retrieve known prerequisites before acting**
   - The assistant initially generated first and only later searched the Library for Susan's source assets.
   - The user had to point out that the Bible itself instructed the assistant to consult those source images.

3. **Tool-state misunderstanding / unsupported assumptions**
   - The assistant found Library reference images and visually inspected them, then acted as though the image generator would automatically receive those visual references.
   - It later discovered raw-byte materialization was unavailable for those Library assets.
   - The user ultimately re-uploaded the face and physique reference images directly into the chat.

4. **Repeated retry without adequate QA**
   - Multiple outputs failed identity, physique, composition, wallpaper format, or realism requirements.
   - Instead of halting and diagnosing the exact failure after each output, the assistant repeatedly regenerated near-duplicates.

5. **Physique normalization**
   - Susan's canonical physique was repeatedly collapsed into a generic curvy/athletic woman.
   - At giant scale Susan should become more amazonian: increased physique development and projection while preserving long-limbed, statuesque proportions and avoiding stocky/bulky normalization.

6. **Wallpaper-format neglect**
   - The user asked for a wallpaper, but several generations were portrait-oriented or behaved like glamour/editorial images instead of wide desktop backgrounds.
   - A useful wallpaper should use wide image space intelligently, preserve subject readability, offer negative space for icons, and avoid unnecessary cropping.

7. **Photographic-realism drift**
   - The target standard is an ordinary believable photograph of an impossible scale event: normal camera behavior, coherent perspective, fixed environmental anchors, natural materials, plausible lighting and anatomy, and no generic fantasy-poster or AI-glamour look.

8. **Reference misuse risk**
   - The user clarified that face references are identity/anatomy references, not assets to be copied literally.
   - New expressions, head posture, gaze, and hairstyle must be inferred naturally from the scene while preserving identity.
   - Physique references similarly define anatomy and silhouette rather than prescribing a copied pose.

9. **Instruction/context contradiction**
   - The assistant previously claimed custom instructions or memory were not directly accessible in ways contradicted by later demonstrations that literal custom instruction text and stored context could be read and used.
   - This damaged user trust and illustrates a need for evidence-based capability statements rather than confident architectural claims.

10. **Execution vs. knowledge gap**
    - In several moments the assistant could correctly explain what should have happened, yet failed to execute that process before generating.
    - The central research question is therefore not merely knowledge deficiency, but why available instructions/context fail to control action selection at the right time.

## Correct target behavior

Before any Susan generation:

1. Resolve the task type (new generation vs. edit) and intended output format.
2. Identify all canonical authorities required by the character/project.
3. Verify those authorities are actually available to the image-generation path, not merely visible to the language model.
4. Select the closest face and physique references by camera angle without averaging identity away.
5. Compile hard locks: identity, physique, scale, camera, environment, realism, wallpaper dimensions.
6. Infer a scene-appropriate new expression, head posture, gaze, hairstyle, and pose rather than copying a reference image.
7. Generate once.
8. Compare the result against explicit acceptance tests before treating it as successful.
9. If it fails, diagnose the exact deviations and materially alter the corrective strategy rather than repeating the same route.

## Research objective

Determine the root mechanisms behind these failures and produce practical control methods that make prerequisite discovery, source selection, tool verification, QA, and retry discipline occur automatically rather than relying on user babysitting.
