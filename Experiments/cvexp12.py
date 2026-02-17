import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")
(h, w) = img.shape[:2]

# Select 4 points from original image
pts1 = np.float32([[50, 50],
                   [300, 50],
                   [50, 300],
                   [300, 300]])

# Define new positions
pts2 = np.float32([[0, 0],
                   [w, 0],
                   [0, h],
                   [w, h]])

# Get perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
perspective_img = cv2.warpPerspective(img, M, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", perspective_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
