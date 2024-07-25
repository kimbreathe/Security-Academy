import socket

print("send start...")
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_socket.connect(("172.17.0.2", 8001))

data_to_send = b"Hello!\n"
client_socket.send(data_to_send)

exit()