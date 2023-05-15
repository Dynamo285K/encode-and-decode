import PIL
from PIL import Image
import PIL
from PIL import Image
pic = Image.open("pic_with_mes.png")
pixels = pic.load()
lenght = 8
width = pic.size[0]
height = pic.size[1]



def getting_blue():
    global zoz
    zoz = []
    for y in range(height):
        for x in range(width):
            pixelblue = pixels[x,y][2]
            blue = bin(pixelblue)
            zoz.append(blue[-1])
    return zoz



getting_blue()

def decoding(zoz):
    message = ""
    number = ""
    for znak in zoz:
        x = ""
        number += znak
        if len(number) == lenght:
            x = chr(int(number,2))
            message += x
            number = ""
        if "#" in message:
            break
    return message

# import PIL
# from PIL import Image
#
# pic = Image.open("pic_with_mes.png")
# pixels = pic.load()


print(decoding(zoz))
