# -*- coding: utf-8 -*-
"""final_project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RqdF9yzSadCzzKeQrw4PHb3FASo_Gbzn
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
import mapper

image = cv2.imread("bill.jpg")
image = cv2.resize(image,(1500,800))
original = image.copy()
plt.imshow(original)

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
from google.colab.patches import cv2_imshow
plt.imshow(gray , cmap="binary")
plt.title("Gray image")

blurred = cv2.GaussianBlur(gray,(5,5),0)
plt.imshow(blurred , cmap="binary")
plt.title("Gaussian Blur")

edge = cv2.Canny(blurred,0,50)
plt.imshow(edge)
plt.title("Edge detection")

contours, hierarchy = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours=sorted(contours,key=cv2.contourArea,reverse=True)

for c in contours:
  p=cv2.arcLength(c,True)
  approx=cv2.approxPolyDP(c,0.02*p,True)

  if len(approx)==4:
    target = approx
    break

approx=mapper.mapp(target)

pts = np.float32([[0,0],[800,0],[800,800],[0,800]])
op=cv2.getPerspectiveTransform(approx,pts)
dst=cv2.warpPerspective(original,op,(800,800))

plt.imshow(dst)