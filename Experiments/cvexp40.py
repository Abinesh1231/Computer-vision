import cv2

# Load image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-17 225539.png")

if img is None:
    print("Image not found")
    exit()

# Manually define rectangle coordinates (example)
# Format: x, y, width, height
x, y, w, h = 60, 40, 180, 250

# Draw rectangle
cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Extract object (crop ROI)
object_crop = img[y:y+h, x:x+w]

# Show results
cv2.imshow("Image with Rectangle", img)
cv2.imshow("Extracted Object", object_crop)

cv2.waitKey(0)
cv2.destroyAllWindows()
