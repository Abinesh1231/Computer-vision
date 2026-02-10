import cv2

# Read image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144335.png")

# Scale factors
bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

# Display results
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
