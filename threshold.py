import numpy as np
import cv2
import math
from matplotlib import pyplot as plt

image = cv2.imread('doc_shadow.png',0)
aaa,th1 = cv2.threshold(image, 50 , 255 , cv2.THRESH_BINARY)
th2 =cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,7 ,4)
th2_1 =cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY ,7 ,4)
th3 =cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,9 ,3)
th4 =cv2.adaptiveThreshold(image,255, cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY ,11 ,1)
cv2.imwrite('th1.jpg', th1);

cv2.imwrite('th2.jpg', th2);
cv2.imwrite('th2_1.jpg', th2_1);
cv2.imwrite('th3.jpg', th3);
cv2.imwrite('th4.jpg', th4);

plt.plot(121),plt.imshow(th1, cmap = 'gray')
plt.title("threshhold output"), plt.xticks([]), plt.yticks([])
plt.show();
plt.plot(122),plt.imshow(th2, cmap = 'gray')
plt.title("addaptive th output"), plt.xticks([]), plt.yticks([])

plt.show();
plt.plot(122),plt.imshow(th3, cmap = 'gray')
plt.title("addaptive th output"), plt.xticks([]), plt.yticks([])
plt.show();

plt.show();
plt.plot(122),plt.imshow(th4, cmap = 'gray')
plt.title("addaptive th output"), plt.xticks([]), plt.yticks([])
plt.show();

cv2.waitKey(0)
