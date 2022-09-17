import socket
import threading
from urllib import request

ip = '127.0.0.1'
port = 5015

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((ip, port))
servidor.listen(5)

print ('Escutando %s:%d' %(ip, port))

def cliente(client_socket):
    request = client_socket.recv(1024)
    print ('Recebidos: %s' %request)
    print ('\n---------------------------')
    client_socket.send(b'Mensagem destina ao cliente.')
    client_socket.close()

while True:
    client, addr = servidor.accept()
    print('[*] Conexao aceita do: %s:%d' %(addr[0], addr[1]))
    client_handler = threading.Thread(target=cliente, args=(client,))
    client_handler.start()
