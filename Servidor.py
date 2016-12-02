#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Programa Servidor
# Fuente original de este codigo: www.pythondiario.com
# Utilizado para fines academicos en el curso CI-1320 

import socket
import sys
import json
import readFile
import random
from queue import Queue



def getFortune():
    #this could work better by using info from the username to generate number
    lineNumber = random.randrange(0, 81)
    fortune = readFile.readLine(lineNumber)
    return fortune
#--load config--
def loadConfig(path):
    with open(path) as configFile:
            config = json.load(configFile)
    host = config["host"]
    port = config["port"]
    recvWindow = config["recvWindow"]
    maxConnections = config["maxConnections"]
    timeout = config["timeout"]
    return host, port, recvWindow, maxConnections, timeout

#--Create TCP/IP socket
def createSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#--Create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#--Create Server
def createServer(socket, host, port):
    server_address = (host, port)
    print ('Launching server {0}:{1}'.format(host, port))
    sock.bind(server_address)
    return sock
#--handle request--
def handleRequest(client_address, recvWindow, connectionQueue):
    try:
            connection = connectionQueue.dequeue()
            
          
            #--Get request and transmit response
            while True:
                data = connection.recv(recvWindow).decode("utf-8")
                print('got {}'.format(data))
                if data:
                    fortune = getFortune()
                    print('Sending response for {0}. Response is {1}'.format(data, fortune))
                    connection.sendall(fortune.encode("utf-8"))
                else:
                    break
    finally:
            pass

def main():
    host, port, recvWindow, maxConnections, timeout = loadConfig("config.json")
    #--create Queue--
    connectionQueue = Queue()
    sock = createSocket()
    sock = createServer(sock, host, port)
    #--Listen for incoming connections. Max is defined in configFile by maxConnections--
    sock.listen(5)
    notClosed = True
    while notClosed:
        # Waiting for connections
        if(connectionQueue.isEmpty()):
            print('Waiting...')
        connection, client_address = sock.accept()
        connectionQueue.enqueue(connection)
        handleRequest(client_address, recvWindow, connectionQueue)

if __name__ == '__main__':
    main()
