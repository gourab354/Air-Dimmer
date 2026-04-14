import cv2
import mediapipe as mp
import math
import socket
import time

ESP32_IP = "192.168.xx.xxx"
ESP32_PORT = 80

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

prev_value = -1

def send_value(val):
    try:
        s = socket.socket()
        s.connect((ESP32_IP, ESP32_PORT))
        s.send(str(val).encode())
        s.close()
    except:
        pass

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm = handLms.landmark

            x1, y1 = int(lm[4].x * 640), int(lm[4].y * 480)
            x2, y2 = int(lm[8].x * 640), int(lm[8].y * 480)

            length = math.hypot(x2 - x1, y2 - y1)

            # better mapping
            brightness = int((length - 30) / (200 - 30) * 255)
            brightness = max(0, min(255, brightness))

            #  send only if changed
            if abs(brightness - prev_value) > 5:
                send_value(brightness)
                prev_value = brightness

            cv2.putText(img, f'{brightness}', (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break
