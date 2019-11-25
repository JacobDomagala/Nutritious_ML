from google_images_download import google_images_download
import os

f = open('foodlist.txt', 'r')
foodList = f.readlines()
f.close()

numClass = len(foodList)
print("{} labels".format(numClass))
path = os.path.dirname(os.path.realpath(__file__)) + "\\downloads"
g = google_images_download.googleimagesdownload() 

for i in foodList:
    i = i[:-1]
    g.download({"output_directory" : path, "keywords" : i, "limit":10})