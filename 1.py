#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        conn.send(b"HELLO!!!")

# with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
#     s.bind((HOST, PORT))
#     _, addr = s.recvfrom(1024)
#     s.sendto(b"HELLO!!!", addr)