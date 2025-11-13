import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Disconnected from server.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 5555))

    name = input("Enter your name: ")
    print("🌿 Share your eco-friendly tips below:")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        tip = input()
        message = f"{name}: {tip}"
        client.send(message.encode('utf-8'))

start_client()
