from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from PIL import Image
import sys

from cbc import CBC
from ecb import EBC

def main():
    infile = sys.argv[1]
    EBC(infile)
    CBC(infile)


if __name__ == "__main__":
    main()
