
from PIL import Image
import logging

ascii_char=list("#*ABCDEfghij;:',. ")

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=float(0.2126*r+0.7152*g+0.0722*b)
    unit=(257.0)/length
    return ascii_char[int(gray/unit)]

def image2text(IMG,width):
    im=Image.open(IMG)
    x,y=im.size
    
    height=float(width)/float(x)*float(y)
    im=im.resize((int(width),int(height)),Image.NEAREST)

    txt=''

    for i in range(int(height)):
        for j in range(int(width)):
            txt+=get_char(*im.getpixel((j,i)))
        txt+='\n'
    return txt
