
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('image1.jpg', 0)

kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT, (5, 5))

dilated = cv2.dilate(img, kernel, iterations=1)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title("Original Image")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(dilated, cmap='gray')
plt.title("Dilated Image")
plt.axis('off')

plt.show()
