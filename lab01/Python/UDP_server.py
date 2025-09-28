import socket
import os

localIP     = "172.17.0.2" # container addr
localPort   = 20001
bufferSize  = 1024
chunkSize  = 2048

files = [f for f in os.listdir("..") if os.path.isfile(os.path.join("..", f))]

for f in files:
    print(f)

name = "Server of John Q. Smith"

 # Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 # Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

 # Listen for incoming datagrams
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    filename = bytesAddressPair[0].decode()
    address = bytesAddressPair[1]

    try:
        if filename in files:
            with open(f"../{filename}", "rb") as f:
                chunk = f.read(chunkSize)
                print(chunk.decode())
                if not chunk:
                    break
                UDPServerSocket.sendto(chunk, address)
        UDPServerSocket.sendto(b"__END__", address)

    except:
        print("Wrong client parameters.")

        # Sending a reply to client~
        UDPServerSocket.close()
