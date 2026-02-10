import cv2
import numpy as np

# Open video file or webcam (0 for webcam)
cap = cv2.VideoCapture(r"D:\Movies\Demon_Slayer_Kimetsu_No_Yaiba_Infinity_Castle_2025_HQ_HDTS_720p_HD.mp4")

# Read first frame to get size
ret, frame = cap.read()
(h, w) = frame.shape[:2]

# Define 4 source points
pts1 = np.float32([[100, 100],
                   [w-100, 100],
                   [100, h-100],
                   [w-100, h-100]])

# Define destination points
pts2 = np.float32([[0, 0],
                   [w, 0],
                   [0, h],
                   [w, h]])

# Get perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply perspective transform
    transformed = cv2.warpPerspective(frame, M, (w, h))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
