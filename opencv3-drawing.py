import numpy as np
import cv2


img = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (300,300),(0,0,255), 10) # Drawing line on img, with start and end co-ordinates , color , line-width

cv2.rectangle(img, (15,25), (300,300), (0,255,0), 8) # drawing rectangle on img, with top-left & bottom right co-ordinates , color, width

cv2.circle(img, (300,300), 55, (255,0,0), -1) # drawing circle with centre , radi, color, width [we can use -1 for fill]

pts = np.array([[250,5],[20,300],[100,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], False, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV Tut!',(0,130), font, 1, (255,255,255), 2, cv2.LINE_AA) # writing text on img , with start co-ordinates, font & fontsize, color, 2, etc.

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()