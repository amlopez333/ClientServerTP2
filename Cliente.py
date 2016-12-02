#!/usr/bin/python
# -*- coding: utf-8 -*-
import socket
import sys
import json

#--load config--
def loadConfig(path):
    with open(path) as configFile:
        config = json.load(configFile)
    host = config["host"]
    port = config["port"]
    recvWindow = config["recvWindow"]
    return host, port, recvWindow

#--Create TCP/IP socket--
def createSocket():
    return socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
#--Connect to server--
def connect(sock, host, port):
    server_address = (host, port)
    print('Connect to Fortune Teller! server at {0}:{1}'.format(host, port))
    sock.connect(server_address)
    return sock
def main():
    host, port, recvWindow = loadConfig("clientConfig.json")
    sock = createSocket()
    sock = connect(sock, host, port)
    username = input("Username: ")
    try:
         
        #--Send message--
        message = username
        print("Readoing fortune for: {0}".format(message))
        sock.sendall(message.encode("utf-8"))
     
        #--Wait for message--
        amount_received = 0
        expectedLength = 15
        data = ''
        while (amount_received < 15):
            data += sock.recv(recvWindow).decode("utf-8")
            amount_received += len(data)
            print("Today's fortune is {0}".format(data))
     
    finally:
        print('Disconnecting from {0}:{1}'.format(host, port))
        sock.close()
if __name__ == '__main__':
    main()

