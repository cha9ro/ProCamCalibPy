import numpy as np
import cv2
from setting import *


# create img
unit = 20
ox = 200
oy = 200
whiteImg = np.zeros((PRO_HEIGHT, PRO_WIDTH, 3), dtype = np.uint8)
whiteImg.fill(255)
for h in range(PRO_HEIGHT):
    for w in range(PRO_WIDTH):
        if h % (2*unit) > unit and w % (2*unit) > unit:
            whiteImg[h][w] = 0

# create window
WINDOW_NAME = "window" # window name
cv2.namedWindow(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
cv2.imshow(WINDOW_NAME, whiteImg)
cv2.moveWindow(WINDOW_NAME, WIN_OX, WIN_OY)
cv2.waitKey(0)
cv2.destroyAllWindows()