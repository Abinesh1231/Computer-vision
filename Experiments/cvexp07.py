import cv2

# Open webcam (0 = default camera)
cap = cv2.VideoCapture(0)

print("Press 'n' = Normal | 's' = Slow | 'f' = Fast | 'q' = Quit")
mode = 'n'

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(30) & 0xFF   # normal speed

    if key == ord('s'):
        mode = 's'
    elif key == ord('f'):
        mode = 'f'
    elif key == ord('n'):
        mode = 'n'
    elif key == ord('q'):
        break

    # Speed control
    if mode == 's':
        cv2.waitKey(120)   # slow motion
    elif mode == 'f':
        cap.read()         # skip frame for fast motion

cap.release()
cv2.destroyAllWindows()
