import cv2

image=cv2.imread( 'C:\\Users\My System\Downloads\\kb.png')
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
inverted=255-gray_image
blured_image= cv2.GaussianBlur(inverted,(35, 35), 0)
blur_inverted=255-blured_image
sketch=cv2.divide(gray_image,blur_inverted,scale=250.0)

cv2.imwrite('C:\\Users\My System\Downloads\\comment.png',sketch)