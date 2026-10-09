import cv2
import mediapipe as mp
import random

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

cap = cv2.VideoCapture(0)

choices = ["Rock", "Paper", "Scissors"]

computer_choice = ""
result = "Press SPACE to play"


def get_fingers(hand):
    fingers = []

    if hand.landmark[4].x < hand.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    tips = [8, 12, 16, 20]
    joints = [6, 10, 14, 18]

    for tip, joint in zip(tips, joints):
        if hand.landmark[tip].y < hand.landmark[joint].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def detect_move(fingers):
    total = sum(fingers)

    if total == 0:
        return "Rock"

    if total == 5:
        return "Paper"

    if total == 2 and fingers[1] == 1 and fingers[2] == 1:
        return "Scissors"

    return "Unknown"


def winner(player, computer):
    if player == "Unknown":
        return "Show your hand clearly"

    if player == computer:
        return "Draw!"

    if (
        player == "Rock" and computer == "Scissors"
        or player == "Paper" and computer == "Rock"
        or player == "Scissors" and computer == "Paper"
    ):
        return "You Win!"

    return "Computer Wins!"


while True:
    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    player_move = "Unknown"

    if results.multi_hand_landmarks:
        hand = results.multi_hand_landmarks[0]

        mp_draw.draw_landmarks(
            frame,
            hand,
            mp_hands.HAND_CONNECTIONS
        )

        fingers = get_fingers(hand)
        player_move = detect_move(fingers)

    cv2.putText(
        frame,
        "You: " + player_move,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        "Computer: " + computer_choice,
        (20, 100),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 0, 0),
        2
    )

    cv2.putText(
        frame,
        result,
        (20, 150),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.putText(
        frame,
        "SPACE = PLAY    ESC = EXIT",
        (20, 450),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow("Rock Paper Scissors", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == 32:
        if player_move != "Unknown":
            computer_choice = random.choice(choices)
            result = winner(player_move, computer_choice)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()