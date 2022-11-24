from ast import While
from distutils.spawn import spawn
import socket

t_ip = "localhost"
t_porta = 5002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((t_ip, t_porta))
s.listen()
print('Aguardando')
conn, ender = s.accept()

print('Conectado', ender)

while True:
    data = conn.recv(1024)
    if not data:
        print('Fechando a conexão')
        conn.close()
        break
    conn.sendall(data)