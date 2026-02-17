import cv2
import numpy as np

# Read image
img = cv2.imread(r"D:\Downloads\download.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator in X direction
sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)

# Convert back to uint8
sobelx = cv2.convertScaleAbs(sobelx)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X Edge Detection", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()
