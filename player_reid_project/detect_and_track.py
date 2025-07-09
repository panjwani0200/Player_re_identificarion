from ultralytics import YOLO
import cv2
import os

# Load model
model = YOLO("yolov8n.pt")

# Create output directory if not exists
os.makedirs("output", exist_ok=True)

# Load video
cap = cv2.VideoCapture("input/Soccer_input_720p.mp4")
writer = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist=True, tracker="bytetrack.yaml")

    for r in results:
        if r.boxes is not None:
            for box in r.boxes:
                cls = int(box.cls[0])
                if cls != 0:  # person class
                    continue
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                track_id = int(box.id[0]) if box.id is not None else -1
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'Player {track_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)

    if writer is None:
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        writer = cv2.VideoWriter("output/result.mp4", fourcc, 30.0, (frame.shape[1], frame.shape[0]))

    writer.write(frame)

cap.release()
writer.release()