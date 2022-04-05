# -*- coding: utf-8 -*-
"""Pencil sketch

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zWaQ8dJPAxw5lFh4UAqutVAe6u9182aR
"""

import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread('Dog.jpg')
img = cv2.resize(img,None,fx=0.3,fy = 0.3)
cv2_imshow(img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
inv_img = cv2.bitwise_not(gray)
blurred_inv_img = cv2.GaussianBlur(inv_img, (21, 21), 0)
blurred_gray_img = cv2.bitwise_not(blurred_inv_img)
pencil_sketch = cv2.divide(gray, blurred_gray_img, scale=230.0)
cv2_imshow(pencil_sketch)