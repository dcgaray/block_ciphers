import struct
import sys
import io
import binascii

def main():
    if len(sys.argv) < 2:
        print("Not enough args given")
        pass
    inputFile = sys.argv[1]
    bmp = open(inputFile, 'rb')
    
    print('Type:', bmp.read(2).decode())
    print('Size: %s' % struct.unpack('I', bmp.read(4)))
    print('Reserved 1: %s' % struct.unpack('H', bmp.read(2)))
    print('Reserved 2: %s' % struct.unpack('H', bmp.read(2)))
    print('Offset: %s' % struct.unpack('I', bmp.read(4)))

    print('DIB Header Size: %s' % struct.unpack('I', bmp.read(4)))
    print('Width: %s' % struct.unpack('I', bmp.read(4)))
    print('Height: %s' % struct.unpack('I', bmp.read(4)))
    print('Colour Planes: %s' % struct.unpack('H', bmp.read(2)))
    print('Bits per Pixel: %s' % struct.unpack('H', bmp.read(2)))
    print('Compression Method: %s' % struct.unpack('I', bmp.read(4)))
    print('Raw Image Size: %s' % struct.unpack('I', bmp.read(4)))
    print('Horizontal Resolution: %s' % struct.unpack('I', bmp.read(4)))
    print('Vertical Resolution: %s' % struct.unpack('I', bmp.read(4)))
    print('Number of Colours: %s' % struct.unpack('I', bmp.read(4)))
    print('Important Colours: %s' % struct.unpack('I', bmp.read(4)))    
    bmp.close()

    header = open(inputFile, 'rb')
    result = header.read(58)
    print(f"The following header for {inputFile} is \n{result}\n")

    #SAL, THIS IS WHERE I AM CURRENTLY STUCK AT!!!!!!
    # I NEED TO GET THE HEADER INFO FROM THE BMP FILE
    print("start") # make sure this line appears in console output
    with io.open(inputFile, "rb") as se:
      content = se.read()
    print(binascii.hexlify(content[:58]))


    # vvvvvvv 2-15-222 1pm vvvvvv
    


if __name__ == "__main__":
    main()
