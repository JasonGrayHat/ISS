import socket
class Client():
	def __init__(self,host,port):
		self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.host = host
		self.port = port

	def connect(self):
		self.serverSocket.connect((self.host,self.port))

	def getMessage(self):
		return self.serverSocket.recv(1024).decode('ascii')

	def closeConnection(self):
		self.serverSocket.close()

if __name__ == '__main__':
	myClient = Client("127.0.0.1",5555)
	myClient.connect()
	message = myClient.getMessage()
	myClient.closeConnection()
	print(message)