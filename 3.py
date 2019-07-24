#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            msg = conn.recv(1024)
            if not msg:
                break
            print("client: ", msg)
            conn.send(input('server: ').encode())