import cv2
import numpy as np

# Read image
img = cv2.imread(r"D:\Downloads\images.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define 8-neighbour Laplacian kernel
kernel = np.array([[1, 1, 1],
                   [1, -8, 1],
                   [1, 1, 1]])

# Apply Laplacian filter
laplacian = cv2.filter2D(gray, cv2.CV_64F, kernel)

# Convert to absolute scale
laplacian = cv2.convertScaleAbs(laplacian)

# Sharpen image
sharpened = cv2.subtract(gray, laplacian)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Laplacian Output", laplacian)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
