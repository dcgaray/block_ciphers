import urllib.parse #god bless the Python gods for having a built-in function for just about anything
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cbc import CBC
from onlineCBC import AESCipher, bitFlip




def condifidentialityLimits():
    block_length = 16
    intial_iv = get_random_bytes(16)
    intial_cipher_key = get_random_bytes(16)
    inputQuery = input("Username: ")
    encodedQuery = submit(inputQuery, intial_cipher_key, intial_iv)
    isAdmin = verify(encodedQuery, intial_cipher_key, intial_iv)
    print(f"Non-Byte Flipped result: {isAdmin}")
    #alright, now time to preform a byte flipping attack
    cipherText = AESCipher(intial_cipher_key).encrypt(inputQuery).decode("UTF-8")
    bFlippedText = bitFlip(4,4,cipherText)
    res = AESCipher(intial_cipher_key).decrypt(bFlippedText).decode("UTF-8")
    print(res)


def lmao(t):
    pos = 4
    bit = 4
    raw = b64decode(t)

    list1 = list(raw)
    fBit = list1[pos] ^ bit 
    print(fBit)
    list1[pos] = ord(chr(fBit)) 
    haha = []
    for x in list1:
        temp = x.to_bytes(1, byteorder="big") 
        haha.append(temp)
    raw = b''.join(haha)
    return b64encode(raw)


# str -> URL encoded and AES-128-CBC encrypted string
def submit(query,cipher_key,iv):
    prependStr = "userid=456;userdata="
    appendStr = ";session-id=31337"
    # %3B is the URL encoding of ";"
    # %3D is the URL encoding of "="
    # OKAY, WHEN PRINTING IT DOESN'T LOOK ANY DIFFERNT BUT IT"S BEEN URL-ENCODED = source;trust_me
    urlEncodedQuery = urllib.parse.quote(query)  
    #our CBC function expects our answer to be in bytes
    bytesQuery = bytes(urlEncodedQuery, 'UTF-8')
    #our CBC function naturally uses a PKCS #7 padding
    cbcEncodedQuery = CBC(bytesQuery, cipher_key, iv)
    return cbcEncodedQuery 

def verify(encodedQuery, c_key, ivec):
    #reuse our intial cipher_key an intialization vector
    cipher = AES.new(c_key, AES.MODE_CBC, ivec)

    #bask in the glory that is python.....
    plaintext = cipher.decrypt(encodedQuery).decode('UTF-8')

    #search the plaintext string for admin priviledges
    #HINT: since all ";" & "=" are URL encoded, they don't show up, theoritcally impossible to make this function return true
    res = ";admin=true;" in  plaintext
    return res


def byteFlipAttack(blockIdx, bit, encodedQuery):
    bytesArr = []

    for i in range(len(encodedQuery)):
        if i != blockIdx: 
            num = encodedQuery[i] # when we grab the byte, it becomes an int
        else:
            b = encodedQuery[i]
            flippedBit = (encodedQuery[i]) ^ bit
            num = flippedBit 
        #<int>.to_bytes(length of byte, byteorder)
        temp = num.to_bytes(1, byteorder="big")
        bytesArr.append(temp)

    bStr = b"".join(bytesArr)
    return bStr


