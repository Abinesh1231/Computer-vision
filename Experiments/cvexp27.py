import cv2

img1 = cv2.imread(r"D:\Downloads\images.jpg")
img2 = cv2.imread(r"D:\Downloads\download (1).jpg")

# Check if images loaded
if img1 is None or img2 is None:
    print("Error loading image")
    exit()

# Crop ROI from img1
roi = img1[100:300, 150:350]

# Get destination image size
h2, w2 = img2.shape[:2]

# Define paste position
x, y = 50, 50

# Resize ROI to fit inside img2
roi = cv2.resize(roi, (min(200, w2 - x), min(200, h2 - y)))

# Paste safely
img2[y:y+roi.shape[0], x:x+roi.shape[1]] = roi

# Show result
cv2.imshow("Source Image", img1)
cv2.imshow("Destination Image (After Paste)", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
