import PIL
from PIL import Image
pic = Image.open("pic_with_mes.png")
pixels = pic.load()
lenght = 8
width = pic.size[0]
height = pic.size[1]



def getting_blue():
    global list1
    list1 = []
    for y in range(height):
        for x in range(width):
            pixelblue = pixels[x,y][2]
            blue = bin(pixelblue)
            list1.append(blue[-1])
    #print(list1)
    return list1



getting_blue()

def decoding(list1):
    message = ""
    number = ""
    for znak in list1:
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


print(decoding(list1))
import tkinter as tk
root = tk.Tk()

root.title("tajna sprava")
w = 800
h = 800
canvas = tk. Canvas(width=w, height=h,bg = "white")

def text():
    canvas.create_text(400,400,fill="darkblue",font="Times 20 italic bold",text=decoding(list1))
    canvas.update
text()
canvas.pack()
root.mainloop()
