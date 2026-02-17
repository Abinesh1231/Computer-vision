import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread(r"D:\Downloads\download (1).jpg",0)
# Convert to binary
_, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Define structuring element
kernel = np.ones((5, 5), np.uint8)

# Apply Closing (Dilation + Erosion)
closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Binary Image", binary)
cv2.imshow("Closing Result", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()
