import subprocess
import os
from PIL import Image
from google_drive_downloader import GoogleDriveDownloader as gdd

# gdd.download_file_from_google_drive(file_id='1iytA1n2z4go3uVCwE__vIKouTKyIDjEq',
#                                     dest_path='./data/mnist.zip',
#                                     unzip=True)
f = open('foodlist.txt', 'r')
foodList = f.readlines()
f.close()

numClass = len(foodList)
path = os.path.dirname(os.path.realpath(__file__)) + "\\downloads"

limit = 100
targetDimension = (64, 64)

for i in foodList:
    i = i[:-1]
    subprocess.call("googleimagesdownload --keywords \"{}\" --limit {}".format(i, limit), shell=True)  
    subPath = path + "\\{}".format(i)
    dirs = os.listdir(subPath)
    for file in dirs:
        filePath = subPath + "\\{}".format(file)
        try:
            im = Image.open(filePath)
            f, e = os.path.splitext(filePath)
            imResize = im.resize(targetDimension, Image.ANTIALIAS)
            imResize.save(f + e, 'JPEG', quality=90)
        except:
            im.close()
            os.remove(filePath)
        
        