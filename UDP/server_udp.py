# servidor UDP
# -*- coding: utf-8 -*-
import socket

HOST = ''  # significa que o servidor aceita conexões em todas as interfaces de rede
PORT = 8888

# cria um objeto socket UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# associa o socket a um endereço e porta
s.bind((HOST, PORT))

print('Servidor esperando por mensagens...')

while True:
    # recebe a mensagem e o endereço do remetente
    data, addr = s.recvfrom(1024)
    
    # processa a mensagem recebida
    print('Mensagem recebida de ' + str(addr) + ': ' + data.decode())

    
    # envia a mensagem de volta para o remetente
    s.sendto(data.upper(), addr)
