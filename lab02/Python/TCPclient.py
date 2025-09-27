#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *
import sys  #needed to access the command-line arguments

if len(sys.argv) != 5:
    print(f"Usage: python {sys.argv[0]} <server> <port> <filename on server> <filename on client>")
    sys.exit(1)

serverName = sys.argv[1]            # server name
serverPort = int(sys.argv[2])       # socket server port number
sockBuffer = 1024                   # socket buffer size

def main():
    print(f"Connecting to server {serverName} on port {serverPort}")
    clientSocket = socket(AF_INET,SOCK_STREAM)       # create TCP socket
    clientSocket.connect((serverName, serverPort))   # open TCP connection

    clientSocket.send(sys.argv[3].encode())             # send user's sentence
                                                        # over TCP connection

    with open(sys.argv[4], "wb") as f:
        while True:
            data = clientSocket.recv(sockBuffer)
            print("Received from server: ", data.decode())
            if data == b"__END__":
                break
            f.write(data)
    
    clientSocket.close()            # close TCP connection

main()
