import socket
import threading

HOST = '127.0.0.1'
PORT = 8000

def read(s):
    while True:
        msg = s.recv(1024)
        if not msg:
            break
        print(msg)

def write(s):
    while True:
        msg = input()
        s.send(msg.encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
t1 = threading.Thread(target=read, args=(s,))
t2 = threading.Thread(target=write, args=(s,))
t1.start()
t2.start()
t1.join()
t2.join()