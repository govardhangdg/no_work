#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    msg = s.recv(1024)
    print(msg)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.sendto(b'', (HOST, PORT))
    msg, addr = s.recvfrom(1024)  
    if addr == (HOST, PORT):
      print(msg)
        