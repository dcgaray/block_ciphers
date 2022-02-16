from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import sys


def main():
    #Ex// cipher = AES.new([key], [mode])
    try:
        inputF = sys.argv[1] 
    except: 
        print(f"Usage: main.py [filename].bmp")
        return
    try:
        im = Image.open(inputF, mode="r")
    except:
        print(f"That is not a valid file.")
        return 

    print(im.info)



if __name__ == "__main__":
    main()