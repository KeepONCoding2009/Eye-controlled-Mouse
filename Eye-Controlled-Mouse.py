import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

screen_w, screen_h = pyautogui.size()

prev_x, prev_y = 0, 0
smooth_factor = 5  # higher = smoother but slower

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = face_mesh.process(rgb)
    landmarks_points = output.multi_face_landmarks

    h, w, _ = frame.shape

    if landmarks_points:
        landmarks = landmarks_points[0].landmark

        # eye point
        x = int(landmarks[474].x * w)
        y = int(landmarks[474].y * h)

        screen_x = screen_w * landmarks[474].x
        screen_y = screen_h * landmarks[474].y

        # smoothing
        curr_x = prev_x + (screen_x - prev_x) / smooth_factor
        curr_y = prev_y + (screen_y - prev_y) / smooth_factor

        pyautogui.moveTo(curr_x, curr_y)
        prev_x, prev_y = curr_x, curr_y

        # blink click
        if (landmarks[145].y - landmarks[159].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(0.8)

        cv2.circle(frame, (x, y), 3, (0,255,0), -1)

    cv2.imshow("Eye Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()