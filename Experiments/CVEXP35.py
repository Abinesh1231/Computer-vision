import cv2
import numpy as np

# Read image in grayscale
img = cv2.imread(r"D:\Downloads\images.jpg")

# Define structuring element
kernel = np.ones((9, 9), np.uint8)

# Apply Black-Hat operation
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Black-Hat Result", blackhat)

cv2.waitKey(0)
cv2.destroyAllWindows()
