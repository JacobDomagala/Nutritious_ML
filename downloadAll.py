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
path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "downloads")
pathToChromeDriver = os.path.join(os.path.dirname(os.path.realpath(__file__)), "chromedriver_win32", "chromedriver.exe")
limit = 500
targetDimension = (128, 128)

for i in foodList[2:]:
    i = i[:-1] # remove '\n' character
    subprocess.call("googleimagesdownload --keywords \"{}\" --limit {} --chromedriver {}".format(i, limit, pathToChromeDriver), shell=True)  
    subPath = os.path.join(path, i)
    dirs = os.listdir(subPath)
    for file in dirs:
        filePath = os.path.join(subPath, file)
        try:
            im = Image.open(filePath)
            f, e = os.path.splitext(filePath)
            imResize = im.resize(targetDimension, Image.ANTIALIAS)
            imResize.save(f + e, 'JPEG', quality=90)
        except:
            im.close()
            os.remove(filePath)
        