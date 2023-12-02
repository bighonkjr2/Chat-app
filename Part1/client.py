# Step 1: Import the socket module
import socket

# Step 2: Create a UDP/IP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Step 3: Define server address and port
server_address = ('localhost', 12345)

# Step 4: Send data
message = 'This is the message. It will be echoed back.'
try:
    while True:
        user_input = input("Enter your message:")
        # Send data
        sent = client_socket.sendto(user_input.encode(), server_address)

finally:
    # Step 6: Close the socket
    print("Closing socket")
    client_socket.close()
