import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread(r"D:\Downloads\download.jpg")

# Convert to binary
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define structuring element (kernel)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated = cv2.dilate(binary, kernel, iterations=1)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
