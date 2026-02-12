import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# -------------------------------
# Counter-Based Edge Detection
# -------------------------------
def counter_edge_detection(image, threshold=100):

    # Sobel gradients
    sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Gradient magnitude
    magnitude = np.sqrt(sobelx**2 + sobely**2)
    magnitude = np.uint8(np.clip(magnitude, 0, 255))

    # Thresholding
    edges = np.zeros_like(magnitude)
    edges[magnitude > threshold] = 255

    # Count edge pixels
    edge_count = np.sum(edges == 255)

    return magnitude, edges, edge_count


# -------------------------------
# Select Image Using File Dialog
# -------------------------------
Tk().withdraw()  # Hide main tkinter window
file_path = askopenfilename(title="Select an Image")

if file_path:

    # Read image as grayscale
    img = cv2.imread(r"C:\Users\Abinesh\OneDrive\Pictures\Screenshots\Screenshot 2026-02-10 145252.png")

    magnitude, edges, count = counter_edge_detection(img)

    print("Selected Image:", file_path)
    print("Number of Edge Pixels:", count)

    # Display Results
    plt.figure(figsize=(12,4))

    plt.subplot(1,3,1)
    plt.title("Original Image")
    plt.imshow(img, cmap='gray')
    plt.axis("off")

    plt.subplot(1,3,2)
    plt.title("Gradient Magnitude")
    plt.imshow(magnitude, cmap='gray')
    plt.axis("off")

    plt.subplot(1,3,3)
    plt.title("Counter-Based Edges")
    plt.imshow(edges, cmap='gray')
    plt.axis("off")

    plt.show()

else:
    print("No image selected.")
