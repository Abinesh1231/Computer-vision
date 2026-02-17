import cv2
import numpy as np

# Read image
img = cv2.imread(r"D:\Downloads\download.jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Define Laplacian kernel (positive center)
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

# Apply sharpening filter directly
sharpened = cv2.filter2D(gray, -1, kernel)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
