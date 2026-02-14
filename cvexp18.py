import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144706.png")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Sobel operator in Y direction
sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Convert to uint8 for display
sobely = cv2.convertScaleAbs(sobely)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Y Edge Detection", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
