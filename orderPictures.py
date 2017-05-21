import os, time
from datetime import datetime
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def createDirsIfNeeded(neededDirPath):
    if not os.path.exists(neededDirPath):
        os.makedirs(neededDirPath)

def formatMonth(month):
    return {
        1: "01_Januar",
        2: "02_Februar",
        3: "03_März",
        4: "04_April",
        5: "05_Mai",
        6: "06_Juni",
        7: "07_Juli",
        8: "08_August",
        9: "09_September",
        10: "10_Oktober",
        11: "11_November",
        12: "12_Dezember"
    }[month]


def getPictureDate(filename):
    # first handle as picture and try to get the date where picture was taken
    image = Image.open(filename)
    info = image._getexif()
    if info is not None:
        #print(info)
        for tag, value in info.items():
            key = TAGS.get(tag, tag)
            if (key == "DateTime"):
                asDateObject = datetime.strptime(value, '%Y:%m:%d %H:%M:%S')
                #print("date of picture: ", asDateObject)
                #print("type: ", type(asDateObject))
                return asDateObject
    #### else ####
    # no picture information is available, use general file information
    st = os.stat(filename)
    asDateObject = datetime.fromtimestamp(st.st_mtime)
    #print("date of file: ", asDateObject)
    #print("type: ", type(asDateObject))
    return asDateObject

def orderPicture(filename):
    pictureData = getPictureDate(filename)
    #print(pictureData)
    neededDirPath = str(pictureData.year) + "/" + formatMonth(pictureData.month)
    # create path if necessary
    createDirsIfNeeded(neededDirPath)
    # move picture to correct location
    os.replace(filename, neededDirPath + "/" + filename)

# define file-endings to look for
fileendings = ('.jpg', '.jpeg')

# actually iterate over all files in current directory and order them
files = [f for f in os.listdir('.') if os.path.isfile(f)]
for f in files:
    print(f)
    if (f.lower().endswith(fileendings)):
        orderPicture(f)
