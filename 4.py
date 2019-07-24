import socket
import threading

HOST = '127.0.0.1'
PORT = 8000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)

def accept(s):
    while True:
        conn, addr = s.accept()
        print('connection received')
        clients.append(conn)
        t = threading.Thread(target=msg_rcvd, args=(conn,))
        t.start()


def msg_rcvd(conn):
    while True:
        msg = conn.recv(1024)
        for client in clients:
            client.send(msg)

accept(s)
