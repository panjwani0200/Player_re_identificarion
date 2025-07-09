# Soccer Player Re-Identification (Single Feed)

This project uses YOLOv8 with built-in tracking to detect and re-identify soccer players in a video.

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/your-username/player_reid_project.git
   cd player_reid_project
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Put your input video in the `input/` directory.

4. Run the tracker:
   ```
   python detect_and_track.py
   ```

## Output

- Result saved in `output/result.mp4`

## Notes

- Uses Ultralytics YOLOv8 + ByteTrack
- Designed for re-ID in a single feed video