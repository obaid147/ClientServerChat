#Each client connects to the server and allows you to send and receive messages in real time.

import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

# Handle receiving messages
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"New message: {message.decode('utf-8')}")
        except:
            print("Server Disconnected...")
            break

# Handle sending messages
def send_messages(client_socket):
    while True:
        message = input("Enter message: ")
        client_socket.send(message.encode('utf-8'))

# Main client loop
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print("Connected to the server.")

    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    threading.Thread(target=send_messages, args=(client_socket,)).start()

if __name__ == '__main__':
    start_client()