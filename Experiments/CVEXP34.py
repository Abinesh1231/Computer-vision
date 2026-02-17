import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png", 0)
, 0)

# Define structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Top-Hat operation
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Top-Hat Result", tophat)

cv2.waitKey(0)
cv2.destroyAllWindows()
