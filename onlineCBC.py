#Okay, so I was able to implement my own version of CBC but it won't work as expected
# This code was gotten from Github(https://github.com/kelalaka153/CBC-Bit-Flipping-Attack/blob/main/AES-CBC-Bit-Flip-Attack.py)
# and was modified for our own purposes

from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    
def bitFlip( pos, bit, data):
    raw = b64decode(data)
    list1 = list(raw)

    fBit = list1[pos] ^ bit
    list1[pos] = chr(fBit)
    list2 = [str(x) for x in list1]
    temp = ''.join(list2)
    raw = temp.encode('utf-8')

    return b64encode(pad(raw, AES.block_size))


if __name__ == '__main__':


    ctx = AESCipher(key).encrypt(msg).decode('utf-8')
    print(type(ctx))
    print('Ciphertext      :', ctx)

    ctx = bitFlip(4,4,ctx)

    print('Message...      :', AESCipher(key).decrypt(ctx).decode('utf-8'))