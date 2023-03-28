# servidor TCP
# -*- coding: utf-8 -*-

import socket

# define o endereço IP e a porta que o servidor vai escutar
HOST = '127.0.0.1'
PORT = 8888

# cria um socket TCP/IP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# associa o socket com o endereço e porta definidos anteriormente
s.bind((HOST, PORT))

# define o limite de conexões simultâneas
s.listen(1)

# espera por uma conexão
conn, addr = s.accept()

# exibe a mensagem de conexão estabelecida
print('Conexao estabelecida por', addr)

try:
    # loop infinito para receber e enviar dados
    while True:
        # recebe dados do cliente
        data = conn.recv(1024)
        # se não houver dados, encerra o loop
        if not data:
            break
        # envia os dados recebidos de volta para o cliente
        conn.sendall(data)
finally:
    # encerra a conexão e o socket
    conn.close()
    s.close()
