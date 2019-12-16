import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"#socket.gethostname()
port = 5555
serverSocket.bind((host,port))

serverSocket.listen(5)

while(True):
	print("Waiting for a connection")
	clientSocket,addr = serverSocket.accept()
	print("Got a connection from {}".format(str(addr)))
	message = "You have connected to the server"
	clientSocket.send(message.encode('ascii'))
	clientSocket.close()


serverSocket.close()