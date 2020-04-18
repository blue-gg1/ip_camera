import wget
from datetime import datetime
import os
import requests
import sys

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

x = 1
while True:
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
    filename = dt_string+'.jpg'
    newname = os.path.join('/Users/bluepill/Documents/proj/ipcamrea/photos' , filename)
    photourl = 'http://192.168.1.25:8080/photo.jpg'
    wget.download(photourl , newname)
    fileinfo = os.stat(newname)
    print("/n")
    

    im = Image.open(newname)
    helvetica = ImageFont.truetype("/Users/bluepill/AppData/Local/Microsoft/Windows/Fonts/a_FuturaOrto-Bold.ttf", size=40)
    d = ImageDraw.Draw(im)

    location = (0, 0)
    text_color = (255, 255, 255)
    d.text(location, dt_string, font=helvetica, fill=text_color)

    im.save("/Users/bluepill/Documents/proj/ipcamrea/photos/"+dt_string+".jpg")
x += 1
