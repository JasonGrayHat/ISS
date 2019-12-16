import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5555

serverSocket.connect((host,port))
message = serverSocket.recv(1024)
serverSocket.close()
print(message.decode('ascii'))