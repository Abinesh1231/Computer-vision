import cv2
import numpy as np

# Read image
img = cv2.imread(r"D:\Downloads\download (1).jpg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 1: Blur image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Step 2: Create mask (original - blurred)
mask = cv2.subtract(gray, blur)

# Step 3: Add mask to original
sharpened = cv2.add(gray, mask)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)
cv2.imshow("Unsharp Mask", mask)
cv2.imshow("Sharpened Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()
