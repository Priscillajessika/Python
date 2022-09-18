from http import client
import socket

ip = '127.0.0.1'
port = 5017

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip, port))
client.send(b'Eu criei um servidor')

response = client.recv(4096)
print(response)