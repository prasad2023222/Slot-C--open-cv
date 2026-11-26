
import cv2
import numpy as np

def create_image(width, height):

    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    box_w = width // 10
    box_h = height // 10

    cv2.rectangle(img, (0, 0), (box_w-1, box_h-1), (0, 0, 255), -1)
    cv2.rectangle(img, (width-box_w, 0), (width-1, box_h-1), (0, 255, 0), -1)
    cv2.rectangle(img, (0, height-box_h), (box_w-1, height-1), (255, 0, 0), -1)
    cv2.rectangle(img, (width-box_w, height-box_h), (width-1, height-1), (0, 255, 255), -1)

    cv2.imshow("Four Corner Boxes", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))

create_image(width, height)
