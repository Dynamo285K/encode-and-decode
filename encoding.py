import PIL
from PIL import Image
message = "Zdravim vsetkych bosorakov#"
pic = Image.open("cat.png")
pixels = pic.load()

lenght = 8
width = pic.size[0]
height = pic.size[1]


def make_zeroes(message:str)->list:
    res = []
    for letter in message:
        number = bin(ord(letter))[2:]
        pn = lenght - len(number)
        number = pn*'0' + number
        # print(number)
        for x in number:
            res.append(int(x))
    # print(res)
    return res




# make_zeroes(message)

def grinder(message:str):
    mes_in_bin = make_zeroes(message)
    for i in range(len(mes_in_bin)):
        x = i % width
        y = i // width
        pixelblue = pixels[x,y][2]
        print(pixelblue)
        newblue = int(bin(pixelblue)[2:-1] + str(mes_in_bin[i]),2)
        newcolor = (pixels[x,y][0], pixels[x,y][1], newblue)
        print(pixels[x,y], newcolor)
        pixels[x,y] = newcolor
    pic.save('pic_with_mes.png')
grinder(message)
