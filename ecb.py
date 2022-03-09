from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

blockLen = 16

def ECB(info,cipher_key = get_random_bytes(16)):
    ogLen = len(info) # we must save the original length of information
    paddedInfo = pad(info,blockLen)
    encryptedInfo = aesEcbEncryption(cipher_key, paddedInfo)
    return encryptedInfo

# PKCS #7 specisies that the value of each added byte is the number of bytes that are added.
# AES has a fixed data block size of 16 bits. If our information is divisible by 16 bytes, then 
# we will add an extra block of bytes for padding
def pad(information,block_length):
    info_len = len(information)
    # b"\x00 is da number 1"
    # 1 * k - (lth mod k) <= from RFC 5652 6.3
    pad = b"\x00" * (block_length - (info_len%block_length))
    return (information + pad)


#takes in two bytes strings and XORs all the bits together
def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

#takes a cipher key, and information to encrypt with ECB using AES
#NOTE: the information being passed in must be padded
def aesEcbEncryption(key, information, mode=AES.MODE_ECB):
    aes = AES.new(key,mode)
    new_info = b""

    for i in range(0,len(information), blockLen):
        blk = information[i:i+blockLen] 
        encBlk = aes.encrypt(blk)
        new_info += encBlk 

    #new_info = aes.encrypt(information)
    return new_info