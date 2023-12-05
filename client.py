import socket

host = "127.0.0.1"
port = 10000

if __name__ == '__main__':
    client_socket = socket.socket()
    client_socket.connect((host, port))

    print(f"Je me suis connecté sur le serveur {host} sur le port {port}")

    message = ""
    while message != "deco-serveur":
        message = input("Votre message : ")
        client_socket.send(message.encode())

    client_socket.close()