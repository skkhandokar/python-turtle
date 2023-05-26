import cv2
from sketchpy import canvas
# image=cv2.imread( 'C:\\Users\My System\Downloads\\real.jpeg')
# gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# inverted=255-gray_image
# blured_image= cv2.GaussianBlur(inverted,(35, 35), 0)
# blur_inverted=255-blured_image
# sketch=cv2.divide(gray_image,blur_inverted,scale=250.0)
#
# cv2.imwrite('C:\\Users\My System\Downloads\\realsketch8.jpeg',sketch)
obj=canvas.sketch_from_image( 'C:\\Users\My System\Downloads\\sk1.png')
obj.draw()