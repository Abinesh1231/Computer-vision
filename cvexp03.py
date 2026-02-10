import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 144706.png")

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to Grayscale (required for Canny)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny Edge Detection
edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

# Display Original and Edge-detected images
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Canny Edge Detection (Outline)")
plt.imshow(edges, cmap="gray")
plt.axis("off")

plt.show()