import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")
(h, w) = img.shape[:2]

# Translation values
tx = 100   # move right by 100 pixels
ty = 50    # move down by 50 pixels

# Translation matrix
M = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
moved_img = cv2.warpAffine(img, M, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Moved Image", moved_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
