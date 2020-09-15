import cv2

print(cv2.__version__)

image = cv2.imread(filename=r'C:\Users\barto\PycharmProjects\AI-Computer-Vision-In-Python\01_basicis\assets\bear.jpg')

cv2.imshow(winname='image', mat=image)
cv2.waitKey(delay=0)