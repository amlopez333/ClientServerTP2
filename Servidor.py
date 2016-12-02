#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
import json

#--load config--
with open("config.json") as configFile:
	config = json.load(configFile)
host = config["host"]
port = config["port"]
recvWindow = config["recvWindow"]
maxConnections = config["maxConnections"]
timeout = config["timeout"]
 
#--Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#--Create Server
server_address = (host, port)
print ('Launching server {0}:{1}'.format(host, port))
sock.bind(server_address)

#--Listen for incoming connections. Max is defined in configFile by maxConnections--
sock.listen(maxConnections)
notClosed = True
while notClosed:
    # Waiting for connections
    print('Waiting...')
    connection, client_address = sock.accept()
 
    try:
        print('Incomming connection from {0}'.format(client_address))
 
        #--Get request and transmit response
        while True:
            data = connection.recv(recvWindow).decode()
            print('got {}'.format(data))
            if data:
                print('Sending response')
                connection.sendall(data.encode())
            else:
                print('No data recieved from {}'.format(client_address))
                break
             
        quit = int(input("press 1 to quit"))
        if quit:
                notClosed = False
    finally:
        pass
sock.close()
