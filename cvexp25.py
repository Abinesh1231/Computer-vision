import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-14 154808.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel X and Y
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Compute gradient magnitude
gradient = cv2.magnitude(sobelx, sobely)
gradient = cv2.convertScaleAbs(gradient)

# Sharpen image (add gradient)
sharpened = cv2.add(gray, gradient)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("Gradient Magnitude", gradient)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
