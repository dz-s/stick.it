import cv2
img = cv2.imread("lenna.png")
crop_img = img[0:200, 0:200]
cv2.imwrite('cropped.png', crop_img)
