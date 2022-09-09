from Crypto.Cipher import AES
import json
from base64 import b64encode, b64decode

data = bytes("Boa noite pessoal, consegui", 'utf-8')
key = b64decode('ABEiM0RVZneImQARIjNEVQ==')

cipher = AES.new(key, AES.MODE_CFB)
ct_raw = cipher.encrypt(data)
iv = b64encode(cipher.iv).decode('utf-8')
ct = b64encode(ct_raw).decode('utf-8')
result = bytes(json.dumps({'iv':iv, 'ct':ct, 'aluno':'priscilla'}), 'utf-8')

print (result)