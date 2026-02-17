import cv2
import numpy as np

# Load image
img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-17 224206.png")
height, width = img.shape[:2]

# Load YOLO model (weights & config)
net = cv2.dnn.readNet(
    r"D:\Downloads\yolov3.weights",
    r"D:\Downloads\yolov3.cfg"
)


# Load COCO class names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Convert image to blob
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
net.setInput(blob)

# Get output layer names
layer_names = net.getUnconnectedOutLayersNames()
outputs = net.forward(layer_names)

# Process detections
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.5:
            label = classes[class_id]

            if label == "watch":  # Check for watch
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 2)
                cv2.putText(img, "Watch", (x, y-10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                            (0,255,0), 2)

# Display result
cv2.imshow("Watch Recognition", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
