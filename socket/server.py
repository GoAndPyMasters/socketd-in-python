"""
This program creates a server that listens for incoming connections on a specific IP address and port. 
When a client connects, it prints a message and receives a message from the client, then sends a response back to the client before closing the connection. 

The program uses the socket library to create the server and handle the communication with the client. 
It binds the server to a specific IP address and port, listens for incoming connections, and then establishes a connection with the client. 
After receiving a message from the client, it sends a response and closes the connection.

To use this code as a server, you need to run it on a machine with the specified IP address and port. 
Clients can then connect to this server using the same IP address and port.
"""

import socket

# Set the IP address and port for the server
# you can get this ip by run ifconfig or ipconfig
HOST = '192.168.10.24'
PORT = 9090

# Create a socket object using IPv4 addresses and TCP protocol
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the server to the specified IP address and port
server.bind((HOST, PORT))

# Listen for incoming connections with a queue size of 5
server.listen(5)

# Continuously accept incoming connections
while True:
    # Accept a new connection and get the communication socket and client address
    communication_socket, address = server.accept()
    # Print a message indicating that a connection has been established with the client
    print(f"Connection from {address} has been established!")
    # Receive a message from the client, decode it from bytes to a string, and print it
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from client: {message}")
    # Send a response back to the client after encoding it to bytes
    communication_socket.send(f"Got your message Thanks!".encode('utf-8'))
    # Close the communication socket
    communication_socket.close()
    # Print a message indicating that the connection with the client has been closed
    print(f"Connection with client from {address} has been closed!")