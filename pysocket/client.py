import socket
import time

HOST = 'localhost'
PORT = 9090

socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)


for i in range(50):
    time.sleep(1)
    socket.connect((HOST,PORT))
    socket.send(f"{i} Hello.".encode('utf-8'))
    