from PIL import Image
import sys

from cbc import CBC
from ecb import ECB
from confid import condifidentialityLimits

def main():
    if len(sys.argv) >= 2:
        infile = sys.argv[1]
        task1(infile) 
    task2()

def task1(infile):
    #Task1
    try:
        im = Image.open(infile, mode="r")
    except:
        print(f"That is not a valid file.")
        return 
    info = im.convert("RGB").tobytes()    
    ecbEncryptedInfo = ECB(info)
    cbcEncryptedInfo = CBC(info)

    createNewBMP(im,ecbEncryptedInfo, len(info),"ECB")
    createNewBMP(im,cbcEncryptedInfo, len(info),"CBC")

def createNewBMP(img,encryptedInfo,ogLen,encType):
    newImage = to_RGB(encryptedInfo[:ogLen])
    im2 = Image.new(img.mode, img.size) #create an image that is the same specs as the original image
    im2.putdata(newImage)
    im2.save(encType + "result.BMP", "BMP")

#maps the orignal image to RGB information
# a lot of magic happens here, just bask in the glory that is python
def to_RGB(information):
    r, g, b = tuple(
        map(
            lambda d: 
            [information[i] for i in range(0,len(information)) if i % 3 == d], [0,1,2])
        )
    pixels = tuple(zip(r,g,b))
    return pixels

def task2():
    condifidentialityLimits()

if __name__ == "__main__":
    main()
