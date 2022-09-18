import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5007
MESSAGE = b'Boa noite pessoal'

print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))


