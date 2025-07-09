## Project Report: Player Re-ID in Soccer Footage

### Task Chosen
Option 2: Re-Identification in a Single Feed

### Approach
- Used pretrained YOLOv8 for detection.
- Applied ByteTrack for tracking players.
- Maintains consistent player IDs across frames.

### Challenges
- Handling occlusion and reappearance.
- Keeping ID assignments stable without identity switching.

### Future Scope
- Embed feature extraction for cross-video matching.
- Optimize inference with TensorRT or ONNX.