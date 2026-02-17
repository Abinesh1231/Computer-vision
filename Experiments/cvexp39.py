import cv2

# Load image
img = cv2.imread(r"D:\Downloads\free-video-854671.jpg")

if img is None:
    print("Error: Image not found")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load car cascade (make sure file exists in same folder)
car_cascade = cv2.CascadeClassifier("haarcascade_car.xml")

# Check if cascade loaded properly
if car_cascade.empty():
    print("Error: Could not load haarcascade_car.xml")
    exit()

# Detect vehicles
cars = car_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=3,
    minSize=(30, 30)
)

# Draw bounding boxes
for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display result
cv2.imshow("Vehicle Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
