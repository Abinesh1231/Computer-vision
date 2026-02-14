import cv2
import numpy as np

# Read image
img = cv2.imread(r"D:\Downloads\download (1).jpg")   # Read as grayscale

# Convert to binary (thresholding)
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
eroded = cv2.erode(binary, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Eroded Image", eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()
