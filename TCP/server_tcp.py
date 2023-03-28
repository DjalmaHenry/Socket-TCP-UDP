# server tcp 
# -*- coding: utf-8 -*-
import socket

HOST = '127.0.0.1'
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()
print('Conexao estabelecida por', addr)

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        conn.sendall(data)
finally:
    conn.close()
    s.close()
