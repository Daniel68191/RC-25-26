#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: cpm
"""
from socket import *
import os
import sys  #needed to access the command-line arguments

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <port>")
    sys.exit(1)

serverPort = int(sys.argv[1])  # socket server port number
sockBuffer = 1024

files = [f for f in os.listdir("..") if os.path.isfile(f)]

def main():
    serverSocket = socket(AF_INET,SOCK_STREAM)   # create TCP welcoming socket
    serverSocket.bind(("", serverPort))

    serverSocket.listen(1)                      # begin listening for incoming TCP requests
    print(f"Server is running on port {serverPort}")

    while True:
        connSocket, addr = serverSocket.accept()    # waits for incoming requests:
                                                    # new socket created on return
        print("Connected by: ", str(addr))

        filename = connSocket.recv(sockBuffer).decode()     # read a sentence of bytes
                                                            # received from client
        try:
            if filename in files:
                with open(f"../{filename}", "rb") as f:
                    chunk = f.read(sockBuffer)
                    print(chunk.decode())
                    if not chunk:
                        break
                    connSocket.send(chunk)
            connSocket.send(b"__END__")

        except:
            print("Wrong client parameters.")

        connSocket.close()      # close TCP connection:
                                # the welcoming socket continues

main()
