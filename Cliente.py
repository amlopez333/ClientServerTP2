#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Cliente
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
timeout = config["timeout"]

username = input("Username: ")

#--Create TCP/IP socket--
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#--Connect to server--
server_address = (host, port)
print('Connect to server at {0}:{1}'.format(host, port))
sock.connect(server_address)
try:
     
    #--Send message--
    message = username
    print("sending message: {0}".format(message))
    sock.sendall(message.encode())
 
    #--Wait for message--
    amount_received = 0
    while amount_received < 4:
        data = sock.recv(recvWindow)
        amount_received += len(data)
        print("getting data: {0}".format(data).decode())
 
finally:
    print('Disconnecting from {0}:{1}'.format(host, port))
    sock.close()


