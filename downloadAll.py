import subprocess
import os

f = open('foodlist.txt', 'r')
foodList = f.readlines()
f.close()

numClass = len(foodList)
print("{} labels".format(numClass))
path = os.path.dirname(os.path.realpath(__file__)) + "\\downloads"

limit = 100

for i in foodList:
    i = i[:-1]
    subprocess.call("googleimagesdownload --keywords \"{}\" --limit {}".format(i, limit), shell=True)  