import cv2

# Open video file
cap = cv2.VideoCapture(r"D:\Movies\Demon_Slayer_Kimetsu_No_Yaiba_Infinity_Castle_2025_HQ_HDTS_720p_HD.mp4")

frames = []

# Read all frames
while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Play frames in reverse order
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
