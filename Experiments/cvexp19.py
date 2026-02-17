import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Sobel X
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Gradient magnitude
sobel_xy = cv2.magnitude(sobelx, sobely)

# Convert to uint8
sobel_xy = cv2.convertScaleAbs(sobel_xy)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel XY Edge Detection", sobel_xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
