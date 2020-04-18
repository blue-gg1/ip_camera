import wget
from datetime import datetime
import os
import image_tools
import requests
import base64
import sys

urlphoto = 'http://192.168.1.33:8080/photoaf.jpg
ph = requests.get(urlphoto)
foto = ph.text
print(sys.getsizeof(foto))
print(ph)

# x = 1
# while True:
#     now = datetime.now()
#     dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
#     filename = dt_string+'.jpg'
#     newname = os.path.join('/Users/bluepill/Documents/proj/ipcamrea/photos' , filename)
#     photourl = 'http://192.168.1.33:8080/photoaf.jpg'
#     wget.download(photourl , newname)
#     fileinfo = os.stat(newname)
#     print(fileinfo.st_size)
    
#     stam = os.system('cat %newname')
#     print(stam)
# x += 1



