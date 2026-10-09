# Rock Paper Scissors with Hand Gesture Recognition

A real-time **Rock Paper Scissors** game in **Python**. The webcam reads your hand gesture with **MediaPipe Hands**, the computer picks a random move, and the result is shown on screen.

## How it works

1. OpenCV captures video from the webcam, and MediaPipe detects one hand and its 21 landmarks.
2. The script checks which fingers are up (comparing each fingertip with its lower joint).
3. The finger pattern becomes a move:

| Gesture | Fingers up | Move |
|---|---|---|
| Closed fist | 0 | Rock |
| Open hand | 5 | Paper |
| Index and middle finger | 2 | Scissors |

4. Press `SPACE` to play a round. The computer chooses randomly and the screen shows **You Win!**, **Computer Wins!** or **Draw!**. If the hand is not clear, it asks you to show it again.
5. Press `ESC` to exit.

## Run it

Requires Python 3.9 or later and a webcam.

```bash
pip install -r requirements.txt
python rock_paper_scissors.py
```

## Files

```
├── rock_paper_scissors.py
├── requirements.txt
└── README.md
```

## Skills demonstrated

Python, computer vision, real-time hand tracking (MediaPipe), OpenCV, game logic.
