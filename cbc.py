from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def CBC(info,cipher_key=get_random_bytes(16), iv=get_random_bytes(16)):
    ogLen = len(info) # we must save the original length of information
    blockLen = 16
    paddedInfo = pad(info,blockLen)
    mode = AES.MODE_CBC
    encryptedInfo = aesCbcEncryption(cipher_key, paddedInfo, iv, mode)
    return encryptedInfo

# PKCS #7 specisies that the value of each added byte is the number of bytes that are added.
# AES has a fixed data block size of 16 bits. If our information is divisible by 16 bytes, then 
# we will add an extra block of bytes for padding
def pad(information,block_length):
    info_len = len(information)
    # b"\x00 is da number 1"
    # 1 * k - (lth mod k) <= from RFC 5652 6.3
    pad = b"\x00" * (block_length - (info_len % block_length))
    return (information + pad)

#takes a cipher key, and information to encrypt with ECB using AES
#NOTE: the information being passed in must be padded
def aesCbcEncryption(key, information, iv, mode=AES.MODE_CBC):
    aes = AES.new(key,mode,iv)


    #take stevens advice and do this yourself, using every resulting ciphertext to XOR the next
    ####Yeah this is cool, but like you're not doing it yourself


    new_info = aes.encrypt(information)
    return new_info
