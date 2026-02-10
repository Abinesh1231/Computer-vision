import cv2

# Read captured video
cap = cv2.VideoCapture(r"D:\Movies\Demon_Slayer_Kimetsu_No_Yaiba_Infinity_Castle_2025_HQ_HDTS_720p_HD.mp4")

print("Press 'n' for Normal, 's' for Slow, 'f' for Fast, 'q' to Quit")

mode = 'n'   # default mode

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

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
        cv2.waitKey(100)     # slow motion
    elif mode == 'f':
        cap.read()           # skip frame → fast motion

cap.release()
cv2.destroyAllWindows()
