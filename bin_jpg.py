import cv2
import numpy as np

img = np.fromfile("/home/pej/Desktop/center/result_0.bin", dtype=np.uint8)

img_sum = img.sum()
avg = img_sum / len(img)
print("sum: ", img_sum)
print(avg)

img = np.reshape(img, (480, 640, 3))

# cv2.imshow('_', img)
# cv2.waitKey(0)