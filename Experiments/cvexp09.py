import cv2

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")
(h, w) = img.shape[:2]

# Image center
center = (w // 2, h // 2)

# Counter-clockwise rotation (45 degrees)
ccw = cv2.getRotationMatrix2D(center, 45, 1.0)
rot_ccw = cv2.warpAffine(img, ccw, (w, h))

# Clockwise rotation (45 degrees)
cw = cv2.getRotationMatrix2D(center, -45, 1.0)
rot_cw = cv2.warpAffine(img, cw, (w, h))

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Counter Clockwise", rot_ccw)
cv2.imshow("Clockwise", rot_cw)

cv2.waitKey(0)
cv2.destroyAllWindows()
