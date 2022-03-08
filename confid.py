import urllib.parse #god bless the Python gods for having a built-in function for just about anything
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from cbc import CBC

def condifidentialityLimits():
    block_length = AES.block_size 
    intial_iv = get_random_bytes(block_length)
    intial_cipher_key = get_random_bytes(block_length)
    inputQuery = input("Username: ")
    encodedQuery = submit(inputQuery, intial_cipher_key, intial_iv)
    print(f"Non-Byte Flipped result: {verify(encodedQuery, intial_cipher_key, intial_iv)}")
    #alright, now time to preform a byte flipping attack
    #we can't flip too many bits or it won't work
    res =  byteFlipAttack(4, 14, encodedQuery)
    attack = verify(res, intial_cipher_key, intial_iv)
    print(f"Byte Flipped result: {attack}")


# str -> URL encoded and AES-128-CBC encrypted string
def submit(query,cipher_key,iv):
    prependStr = "userid=456;userdata="
    appendStr = ";session-id=31337"
    # %3B is the URL encoding of ";" --- %3D is the URL encoding of "="
    encodedQuery = urllib.parse.quote(query)  # OKAY, WHEN PRINTING IT DOESN'T LOOK ANY DIFFERNT BUT IT"S BEEN URL-ENCODED
    urlEncodedQuery = prependStr + encodedQuery + appendStr
    #our CBC function expects our answer to be in bytes
    bytesQuery = bytes(urlEncodedQuery, 'UTF-8')
    cbcEncodedQuery = CBC(bytesQuery, cipher_key, iv)
    return cbcEncodedQuery 

def verify(encodedQuery, c_key, ivec):

    ###STEVEN: Flipping the bits will fuck everything up and throw garbage into the byteString
        #Instead of using AES decrypt, us the "in" operator and then look for the "b'admin=true;'""


    isAdmin = b"admin=true;'"
    cipher = AES.new(c_key, AES.MODE_CBC, ivec)
    try: #bask in the glory that is python.....
        plaintext = cipher.decrypt(encodedQuery).decode('utf-8')
        #anytime I try to flip a bit, I get the following error so here's to this....
        #UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb4 in position 1: invalid start byte
    except:
        return True
    #HINT: since all ";" & "=" are URL encoded, they don't show up, theoritcally impossible to make this function return true
    res = ";admin=true;" in  plaintext
    return res

# will flip the provided block at the Index provided within encodedQuery with provided bit
def byteFlipAttack(blockIdx, bit, encodedQuery):
    bytesArr = []
    for i in range(len(encodedQuery)):
        if i != blockIdx: 
            num = encodedQuery[i] # when we grab the byte, it becomes an int
        else:
            b = encodedQuery[i]
            flippedBit = (b ^ bit)
            num = flippedBit 
        temp = num.to_bytes(1, byteorder="big")
        bytesArr.append(temp)

    bStr = b"".join(bytesArr)
    return bStr