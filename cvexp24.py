import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-14 154808.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Choose boost factor (A >= 1)
A = 1.5

# Create high-boost kernel (4-neighbour)
kernel = np.array([[0, -1, 0],
                   [-1, A+4, -1],
                   [0, -1, 0]])

# Apply filter
highboost = cv2.filter2D(gray, -1, kernel)

# Display results
cv2.imshow("Original Image", gray)
cv2.imshow("High-Boost Sharpened Image", highboost)

cv2.waitKey(0)
cv2.destroyAllWindows()
