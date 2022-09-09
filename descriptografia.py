import json
from base64 import b64decode
from Crypto.Cipher import AES

json_input='{"iv": "tUnxb1PKKkLvI0E+pOsmAg==", "ciphertext": "yleuoKxlbrIkil6DB/XMFUxzVvKhU06EI4iKUXZrG+Xqi7Z9BgWZjQ=="}'
key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

try:

    b64 = json.loads(json_input)
    iv = b64decode(b64['iv'])
    ct = b64decode(b64['ciphertext'])
    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    text = cipher.decrypt(ct)

    print("The message was: ", str(text, 'utf-8'))

except (ValueError, KeyError):

    print("Incorrect decryption")