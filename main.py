from PIL import Image
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import sys

from cbc import CBC
from ecb import ECB
from confid import condifidentialityLimits

def main():
    block_length = AES.block_size 
    cipher_key = get_random_bytes(16)    
    iv = get_random_bytes(16)    

    inputQuery = input("message: ") 
    #our ECB function expects our answer to be in bytes
    bytesQuery = bytes(inputQuery, 'UTF-8')

    '''
    ecbQuery = ECB(bytesQuery,cipher_key)
    cipher = AES.new(cipher_key, AES.MODE_ECB)
    plaintext = cipher.decrypt(ecbQuery).decode('utf-8')
    print(plaintext)
    '''

    cbcQuery = CBC(bytesQuery, cipher_key, iv)
    print(f"{cbcQuery} <- text and then it's a {type(cbcQuery)}")
    cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(cbcQuery).decode('utf-8')
    print(plaintext)

    '''
    if len(sys.argv) >= 2:
        infile = sys.argv[1]
        task1(infile) 
    task2()
    '''

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
