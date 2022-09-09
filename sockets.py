import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 7777
MESSAGE = b'{"iv": "1vwUc9XGJbIg1s/Uhew+kg==", "ct": "t+yxXELTQjjS0dz/EsSyOvngQOTTh6TM8VbN", "aluno": "priscilla"}'

#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, 
socket.SOCK_DGRAM, socket.IPPROTO_UDP)

sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
