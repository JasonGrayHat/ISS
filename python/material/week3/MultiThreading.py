import threading,time

class myThread(threading.Thread):
	threadCount = 0

	def __init__(self,name):
		super().__init__()
		self.name = name
		myThread.threadCount+=1

	def run(self):
		time.sleep(5)
		threadLock.acquire()
		print("Hello from thread",self.name)
		threadLock.release()
		
		
threadLock = threading.Lock()

threads = []

if __name__ == '__main__':
	for i in range(50):
		threads.append(myThread(i))

	for thread in threads:
		thread.start()

	for thread in threads:
		thread.join()
	print(myThread.threadCount)
