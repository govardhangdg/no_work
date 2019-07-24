import socket

HOST = '127.0.0.1'
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        msg = input('client: ')
        if not msg:
            break 
        s.send(msg.encode())
        msg = s.recv(1024)
        print('server: ', msg)
        
