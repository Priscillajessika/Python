from ast import While
from distutils.spawn import spawn
import socket

t_ip = "localhost"
t_porta = 5002

msg = input("Sua mensagem é? ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((t_ip, t_porta))
s.sendall(str.encode(msg))
data = s.recv(1024)

print('Mensagem recebida: ', data.decode())