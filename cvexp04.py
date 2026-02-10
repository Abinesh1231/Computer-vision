import cv2
import numpy as np

# Read the image
image = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 145013.png")   # 0 = grayscale

# Create a kernel (structuring element)
kernel = np.ones((5, 5), np.uint8)

# Apply dilation
dilated_image = cv2.dilate(image, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Dilated Image", dilated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
