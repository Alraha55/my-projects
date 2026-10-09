from ultralytics import YOLO
import cv2
import math
import time

model = YOLO("yolo11n.pt")

video = cv2.VideoCapture("traffic.mp4")

if not video.isOpened():
    print("Video not found")
    exit()

previous_positions = {}
PIXELS_PER_METER = 8

while True:
    success, frame = video.read()

    if not success:
        break

    results = model.track(
        frame,
        persist=True,
        tracker="bytetrack.yaml",
        verbose=False
    )

    for result in results:
        if result.boxes is None:
            continue

        for box in result.boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]

            if class_name not in ["car", "bus", "truck", "motorcycle"]:
                continue

            if box.id is None:
                continue

            track_id = int(box.id[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            speed = 0

            if track_id in previous_positions:
                old_x, old_y, old_time = previous_positions[track_id]

                distance_pixels = math.sqrt(
                    (center_x - old_x) ** 2 +
                    (center_y - old_y) ** 2
                )

                elapsed_time = time.time() - old_time

                if elapsed_time > 0:
                    distance_meters = distance_pixels / PIXELS_PER_METER
                    speed = (distance_meters / elapsed_time) * 3.6

            previous_positions[track_id] = (
                center_x,
                center_y,
                time.time()
            )

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (1, 255, 0),
                2
            )

            cv2.putText(
                frame,
                f"{class_name} ID:{track_id}",
                (x1, y1 - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 2),
                2
            )

            cv2.putText(
                frame,
                f"{speed:.1f} km/h",
                (x1, y1 - 5),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2
            )

    cv2.imshow("Vehicle Speed Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()