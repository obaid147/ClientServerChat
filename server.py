import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = []

# broadcast message to all clients
def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

# handle individual clients
def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Message received: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                print("Disconnected client")
                break
        except:
            break

    # Remove client on disconnect
    clients.remove(client_socket)
    client_socket.close()

# Main server loop
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server started on Host {HOST}:{PORT}")

    while True:
        # accept new client
        client_socket, client_address = server_socket.accept()
        print(f"New connection {client_address}")

        #add client to list
        clients.append(client_socket)

        # Start a new thread to handle this client
        threading.Thread(target=handle_client, args=(client_socket, )).start()

if __name__ == '__main__':
    start_server()
