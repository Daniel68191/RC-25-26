import socket

name = "Client of John Q. Smith"
print("Enter the filename: ")
filename = input()

bytesToSend = str.encode(filename)

serverAddressPort   = ("172.17.0.2", 20001) # container addr 
bufferSize          = 2048

 # Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send the message to server using the UDP socket created
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

with open(filename, "wb") as f:
    while True:
        data, addr = UDPClientSocket.recvfrom(bufferSize)
        print("Received from server: ", data.decode())
        if data == b"__END__":
            break
        f.write(data)

UDPClientSocket.close()