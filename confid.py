from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cbc import CBC
import urllib.parse #god bless the Python gods for having a built-in function for just about anything

iv = get_random_bytes(16)
cipher_key = get_random_bytes(16)


def condifidentialityLimits():
    block_length = 16
    inputStr = input("Username: ")
    paddedStr = submit(inputStr)
    # TODO : FINISH THIS
    print(paddedStr)


# str -> URL encoded and AES-128-CBC encrypted string
def submit(query):
    prependStr = "userid=456;userdata="
    appendStr = ";session-id=31337"
    # %3B is the URL encoding of ";"
    # %3D is the URL encoding of "="
    # OKAY, WHEN PRINTING IT DOESN'T LOOK ANY DIFFERNT BUT IT"S BEEN URL-ENCODED = source;trust_me
    urlEncodedQuery = urllib.parse.quote(query)  

    #our CBC function expects our answer to be in bytes
    bytesQuery = bytes(urlEncodedQuery, 'utf-8')
    cbcEncodedQuery = CBC(bytesQuery, cipher_key, iv)
    return cbcEncodedQuery 

# PKCS #7 specisies that the value of each added byte is the number of bytes that are added.
# AES has a fixed data block size of 16 bits. If our information is divisible by 16 bytes, then 
# we will add an extra block of bytes for padding
def pad(information, block_length):
    info_len = len(information)
    # b"\x00 is da number 1"
    # 1 * k - (lth mod k) <= from RFC 5652 6.3
    pad = b"\x00" * (block_length - (info_len % block_length))
    return (information + pad)

