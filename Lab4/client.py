# client.py

import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Home page
    s.send(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
    data = s.recv(1024)
    print(data.decode())

    # About page
    s.send(b'GET /about HTTP/1.1\r\nHost: localhost\r\n\r\n')
    data = s.recv(1024)
    print(data.decode())

    # Product page
    s.send(b'GET /product/1 HTTP/1.1\r\nHost: localhost\r\n\r\n')
    data = s.recv(1024)
    print(data.decode())