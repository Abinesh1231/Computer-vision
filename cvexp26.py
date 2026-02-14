import cv2

# Read image
img = cv2.imread(r"D:\Downloads\download (1).jpg")

overlay = img.copy()

# Add text on overlay
cv2.putText(overlay, "© Abinesh", (50, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            2, (255, 255, 255), 3)

# Blend images (transparency)
alpha = 0.4
watermarked = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)

# Display result
cv2.imshow("Original",img)
cv2.imshow("Transparent Watermark", watermarked)
cv2.waitKey(0)
cv2.destroyAllWindows()
