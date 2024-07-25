import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8002))
server_socket.listen(1)

print("Listening ...")

client_socket, client_address = server_socket.accept()
print("Connection Accepted!")

data = client_socket.recv(1024)

print(f"Received data: {data.decode('utf-8')}")
client_socket.close()