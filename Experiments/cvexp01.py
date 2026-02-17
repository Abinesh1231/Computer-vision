import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r"C:\Users\Abinesh\OneDrive\Desktop\Screenshot 2026-02-10 140525.png")

if image is None:
    print("Image not loaded. Check file path.")
    exit()

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(image_rgb)
plt.axis("off")

plt.subplot(1, 2, 2)
plt.title("Grayscale")
plt.imshow(gray_image, cmap="gray")
plt.axis("off")

plt.show()
