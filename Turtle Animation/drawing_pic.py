import cv2
import turtle
import numpy as np
from matplotlib import pyplot as plt
import time
turtle.tracer(0)

wnc = turtle.Screen()
wnc.bgcolor('#e2e2e2')

def find_closest(p):
    if len(positions) > 0:
        nodes = np.array(positions)
        distances = np.sum((nodes - p) ** 2, axis=1)
        i_min = np.argmin(distances)
        return positions[i_min]
    else:
        return None


def outline():
    src_image = cv2.imread(image, 0)
    #blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
    blurred = cv2.GaussianBlur(src_image, (7, 7), 0)
      
    th3 = cv2.adaptiveThreshold (src_image, maxValue=257, adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                thresholdType=cv2.THRESH_BINARY, blockSize=9, C=2)
    return th3

image = 'C:\\Users\My System\Downloads\\cr7.jpg'
im = cv2.imread(image, 0)
th3 = outline()

plt.imshow(th3)
plt.axis('off')
plt.tight_layout()
# plt.show()

WIDTH = im.shape[0]
HEIGHT = im.shape[1]
print(WIDTH, HEIGHT)

CUTOFF_LEN = ((WIDTH + HEIGHT) / 2) / 60  # 60 threshold value
iH, iW = np.where(th3 == [0])
iW = iW - WIDTH / 2
iH = -1 * (iH - HEIGHT / 2)
positions = [list(iwh) for iwh in zip(iW, iH)]

# win = turtle.Screen()
# win.bgcolor('black')

t = turtle.Turtle()
t.color("black")
t.shapesize(1)
t.width(1)
t.pencolor('#928c8c')

t.speed(0)
turtle.tracer(0, 0)
t.penup()
t.goto(positions[0])
t.pendown()

time.sleep(1)

p = positions[0]
while (p):
    p = find_closest(p)
    if p:
        current_pos = np.asarray(t.pos())
        new_pos = np.asarray(p)
        length = np.linalg.norm(new_pos - current_pos)
        if length < CUTOFF_LEN:
            t.goto(p)
            turtle.update()
        else:
            t.penup()
            t.goto(p)
            t.pendown()
        positions.remove(p)
    else:
        p = None


time.sleep(1)

turtle.done()
cv2.imwrite('C:\\Users\My System\Downloads\\realsketch8.jpeg',t)