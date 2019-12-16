class Client():
	def __init__(self,host,port):
		pass

	def connect(self):
		pass

	def getMessage(self):
		return None

	def closeConnection(self):
		pass

if __name__ == '__main__':
	myClient = Client("127.0.0.1",5555)
	myClient.connect()
	message = myClient.getMessage()
	myClient.closeConnection()''