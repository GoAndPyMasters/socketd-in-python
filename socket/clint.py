"""
This program creates a client that connects to a server with a specific IP address and port. 
It sends a message to the server and receives a response back.

The program uses the socket library to create the client and establish a connection with the server. 
It then sends a message to the server and receives a response.

To use this code as a client, you need to run it on a machine with access to the specified server IP address and port.
"""

import socket

# Set the IP address and port for the server
HOST = '192.168.10.24'
PORT = 9090

# Create a socket object using IPv4 addresses and TCP protocol
socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server using the specified IP address and port
socket_client.connect((HOST, PORT))

# Send a message to the server after encoding it to bytes
socket_client.send("Hello".encode('utf-8'))

# Receive a response from the server, decode it from bytes to a string, and print it
print(socket_client.recv(1024).decode('utf-8'))