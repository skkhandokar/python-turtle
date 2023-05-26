


import random
from PIL import Image, ImageDraw
def line(image_path, output_path):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    colors = ["red", "green", "blue", "yellow",
              "purple", "orange"]
    for i in range(0, 100, 20):
        draw.line((i, 0) + image.size, width=5,
                  fill=random.choice(colors))
    image.save(output_path)

if __name__ == "__main__":
    line("C:\\Users\My System\Downloads\\udr.JPG", "C:\\Users\My System\Downloads\\all.jpg")