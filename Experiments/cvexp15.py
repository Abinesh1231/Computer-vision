import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")
(h, w) = img.shape[:2]

# Source points (at least 4)
src_pts = np.float32([[50, 50],
                      [300, 50],
                      [50, 300],
                      [300, 300]])

# Destination points
dst_pts = np.float32([[30, 120],
                      [320, 60],
                      [80, 350],
                      [350, 300]])

# Compute homography using DLT
H, _ = cv2.findHomography(src_pts, dst_pts, 0)  # 0 = Direct Linear Transformation

# Apply transformation
dlt_img = cv2.warpPerspective(img, H, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", dlt_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
