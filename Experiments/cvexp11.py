import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 145252.png")
(h, w) = img.shape[:2]

# Select 3 points from original image
pts1 = np.float32([[50, 50],
                   [200, 50],
                   [50, 200]])

# Define their new positions
pts2 = np.float32([[10, 100],
                   [200, 50],
                   [100, 250]])

# Get affine transformation matrix
M = cv2.getAffineTransform(pts1, pts2)

# Apply affine transformation
affine_img = cv2.warpAffine(img, M, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformed Image", affine_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
