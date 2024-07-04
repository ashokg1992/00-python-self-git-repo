
# The first address in each subnet is reserved for the network address, and the last address is reserved for the broadcast address.
 


#     Calculating Subnet Ranges:

#         With the new subnet mask, each subnet will have 64 addresses (2^6).

#         We'll have 4 subnets: 192.168.0.0/26, 192.168.0.64/26, 192.168.0.128/26, and 192.168.0.192/26.

#         Subnet 1 (192.168.0.0/26):
#             Network Address: 192.168.0.0
#             Usable Host Range: 192.168.0.1 - 192.168.0.62
#             Broadcast Address: 192.168.0.63

#         Subnet 2 (192.168.0.64/26):
#             Network Address: 192.168.0.64
#             Usable Host Range: 192.168.0.65 - 192.168.0.126
#             Broadcast Address: 192.168.0.127

#         Subnet 3 (192.168.0.128/26):
#             Network Address: 192.168.0.128
#             Usable Host Range: 192.168.0.129 - 192.168.0.190
#             Broadcast Address: 192.168.0.191

#         Subnet 4 (192.168.0.192/26):
#             Network Address: 192.168.0.192
#             Usable Host Range: 192.168.0.193 - 192.168.0.254
#             Broadcast Address: 192.168.0.255

#         Note: The first address in each subnet is reserved for the network address, and the last address is reserved for the broadcast address.

# This is a basic example of subnetting. In practice, subnetting becomes more complex when dealing with different subnet masks, VLSM (Variable Length Subnet Masking), and routing between subnets. Understanding subnetting is essential for network administrators and engineers.


# ========================================================= SOCKETS =============================

# - Socket Library:
#     it helps to establish connectin b/n server and clienets 
# - server-client communication using the socket library.
# -The server will listen for incoming connections, and the client will connect to the server and send a message.
# -



# import socket

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Define the host and port
# host = '127.0.0.1'  # localhost
# port = 12345

# # Bind the socket to the address
# server_socket.bind((host, port))

# # Start listening for incoming connections
# server_socket.listen(5)

# print(f'Server listening on {host}:{port}...')

# # Accept a connection and get the client socket
# client_socket, client_address = server_socket.accept()
# print(f'Connection established with {client_address}')

# # Receive data from the client
# data = client_socket.recv(1024).decode('utf-8')
# print(f'Received: {data}')

# # Echo the received data back to the client
# client_socket.send(data.encode('utf-8'))

# # Close the sockets
# client_socket.close()
# server_socket.close()


# # =========================================================  request - SOCKETS =============================

import requests

# Make a GET request to a URL
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content (JSON in this case)
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')