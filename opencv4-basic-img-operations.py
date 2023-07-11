import cv2
import numpy as np


img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)

# px = img[300,300]
# px = [0,0,0]

roi = img[900:1000,900:1000]
# roi = [255,255,255]

img[0:100,0:100] = roi


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# print(px)
