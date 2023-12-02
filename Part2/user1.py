import socket
import threading

def create_server(host, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))
    return server

def listen_for_messages(server, buffer_size=1024):
    data, addr = server.recvfrom(buffer_size)
    print(f"\nNickname: {data.decode()} from {addr} joined.")
    nickname = data.decode()
    
    while True:
        data, addr = server.recvfrom(buffer_size)
        msg = data.decode()
        if msg.startswith("/change_nick"):
            nickname = msg[len("/change_nick")+1:]
        else:
            print(f"\n{nickname}: {msg}")

        


def send_message(client, host, port, message):
    client.sendto(message.encode(), (host, port))

# Configuration
user1_ip = '192.168.1.25'
user2_ip = '192.168.1.24'
user1_port = 12345
user2_port = 12346

# Create server and client for user 1
user1_server = create_server(user1_ip, user1_port)
user1_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Start a thread to listen for messages from User 2, will be ran in the background
threading.Thread(target=listen_for_messages, args=(user1_server,)).start()

server_input = input("Enter your nickname:")
send_message(user1_client, user2_ip, user2_port, server_input)

# Example sending a message from user 1 to user 2
while True:
    user1_input = input("Enter your message:")
    send_message(user1_client, user2_ip, user2_port, user1_input)

    if user1_input == "EXIT":
        break

# Remember to close the sockets when done
user1_server.close()
user1_client.close()