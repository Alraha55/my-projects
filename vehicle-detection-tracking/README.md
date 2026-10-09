# Vehicle Detection and Speed Estimation

A computer vision project in **Python** that detects and tracks vehicles in a traffic video using **YOLO11** and **ByteTrack**, and displays an estimated speed for each tracked vehicle.

## What it does

- Reads a traffic video frame by frame with OpenCV
- Detects vehicles with the pretrained **YOLO11n** model (Ultralytics) and keeps only `car`, `bus`, `truck` and `motorcycle`
- Tracks each vehicle across frames with **ByteTrack**, giving it a persistent ID
- Draws a bounding box, the class name and ID, and an estimated speed in km/h above each vehicle
- Press `q` to quit

## How speed is estimated

For each tracked vehicle the script measures how far its center moved between two frames (in pixels), converts pixels to meters with a fixed scale (`PIXELS_PER_METER = 8`), divides by the elapsed time, and converts to km/h.

## Run it

Requires Python 3.9 or later.

```bash
pip install -r requirements.txt
```

Put a traffic video named `traffic.mp4` in the same folder (the video is not included in this repository), then run:

```bash
python traffic_alraha.py
```

The YOLO11n weights (`yolo11n.pt`) are downloaded automatically by Ultralytics on the first run.

## Limitations and ideas for improvement

- Speeds are **estimates**: the pixel-to-meter scale is a fixed constant, not calibrated to the camera view, so real-world accuracy is limited.
- Elapsed time is taken from the computer's clock rather than from the video's frame rate, so the numbers depend on processing speed. Using the video's FPS would make them consistent.
- Next steps: camera calibration, a counting line to count vehicles, and saving the annotated video.

## Files

```
├── traffic_alraha.py     # detection, tracking and speed estimation
├── requirements.txt
└── README.md
```

## Skills demonstrated

Python, computer vision, object detection and multi-object tracking (YOLO11, ByteTrack), OpenCV.
