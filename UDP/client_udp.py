# cliente UDP
# -*- coding: utf-8 -*-
import socket

HOST = 'localhost'  # endereço do servidor
PORT = 8888

# cria um objeto socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# envia uma mensagem para o servidor
s.sendto(b'Ola, servidor!', (HOST, PORT))

# recebe a resposta do servidor
data, addr = s.recvfrom(1024)

# exibe a mensagem recebida
print('Mensagem recebida de ' + str(addr) + ': ' + data.decode())

# fecha a conexão
s.close()
