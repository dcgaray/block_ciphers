from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import sys


def main():
    #Ex// cipher = AES.new([key], [mode])
    try:
        inputF = sys.argv[1] 
        print(f"Alright, i was given [{inputF}], time to encrypt it with AES-CBC")
    except: 
        print(f"Usage: main.py [filename].bmp")
        return
    try:
        im = Image.open(inputF, mode="r")
    except:
        print(f"That is not a valid file.")
        return 
    #Code

    cipher_key = get_random_bytes(16)
    info = im.convert("RGB").tobytes()
    ogLen = len(info) # we must save the original length of information
    blockLen = 16
    paddedInfo = pad(info,blockLen)
    encryptedInfo = aesCbcEncryption(cipher_key, paddedInfo)
    newImage = to_RGB(encryptedInfo[:ogLen])
    im2 = Image.new(im.mode, im.size) #create an image that is the same specs as the original image
    im2.putdata(newImage)
    im2.save("CBCresult.BMP", "BMP")

# PKCS #7 specisies that the value of each added byte is the number of bytes that are added.
# AES has a fixed data block size of 16 bits. If our information is divisible by 16 bytes, then 
# we will add an extra block of bytes for padding
def pad(information,block_length):
    info_len = len(information)
    pad = b"\x00" * (block_length - (info_len%16))
    return (information + pad)

#maps the orignal image to RGB information
def to_RGB(information):
    r, g, b = tuple(
        map(
            lambda d: 
            [information[i] for i in range(0,len(information)) if i % 3 == d], [0,1,2])
        )
    pixels = tuple(zip(r,g,b))
    return pixels

#takes a cipher key, and information to encrypt with ECB using AES
#NOTE: the information being passed in must be padded
def aesCbcEncryption(key, information, mode=AES.MODE_CBC):
    iv = get_random_bytes(16)
    aes = AES.new(key,mode,iv)
    new_info = aes.encrypt(information)
    return new_info

if __name__ == "__main__":
    main()