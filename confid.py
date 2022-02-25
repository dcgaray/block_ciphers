import urllib.parse #god bless the Python gods for having a built-in function for just about anything
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cbc import CBC
from base64 import b64decode




def condifidentialityLimits():
    block_length = 16
    intial_iv = get_random_bytes(16)
    intial_cipher_key = get_random_bytes(16)
    inputQuery = input("Username: ")
    encodedQuery = submit(inputQuery, intial_cipher_key, intial_iv)
    isAdmin = verify(encodedQuery, intial_cipher_key, intial_iv)
    print(f"Non-Byte Flipped result: {isAdmin}")
    print(encodedQuery)
    #alright, now time to preform a byte flipping attack
    flippedQuery = byteFlipAttack(10,7, encodedQuery)
    print(flippedQuery)
    test = verify(flippedQuery, intial_cipher_key, intial_iv)
    print(test)



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
    print(plaintext)

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
            print(type(b))
            flippedBit = (encodedQuery[i]) ^ bit
            num = flippedBit 
        #<int>.to_bytes(length of byte, byteorder)
        temp = num.to_bytes(1, byteorder="big")
        bytesArr.append(temp)


    bStr = b"".join(bytesArr)
    return bStr


