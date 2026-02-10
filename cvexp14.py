import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 145252.png")
(h, w) = img.shape[:2]

# Source points (4 or more points)
src_pts = np.float32([[50, 50],
                      [300, 50],
                      [50, 300],
                      [300, 300]])

# Destination points
dst_pts = np.float32([[10, 100],
                      [320, 40],
                      [80, 350],
                      [350, 300]])

# Compute Homography matrix
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply homography transformation
homography_img = cv2.warpPerspective(img, H, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Homography Transformed Image", homography_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
