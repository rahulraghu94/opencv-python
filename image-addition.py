# -*- coding: utf-8 -*-

import cv2

# Image Blending
# Load any two images and use cv.add module to get result
# Pointless 
img1 = cv2.imread("resource/red.jpg")

img2 = cv2.imread("resource/blue.jpg")

dest = cv2.addWeighted(img2, 0.5, img1, 0.5, 1)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("cv2.add img1 and img2", dest)

cv2.waitKey(0)
cv2.destroyAllWindows()
