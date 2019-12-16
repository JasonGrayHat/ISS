from tkinter import Tk, Button, Entry

class MyGUI(Tk):
	def __init__(self):
		super().__init__()
		self.buildWindow()


	def buildWindow(self):

		myEntry = Entry(self,width = 50)
		myEntry.grid(column = 0,row = 0, columnspan = 10,padx = 5, pady = 5,ipadx = 5, ipady=5)

		for x in range(10):
			for y in range(10):
				tempButton = Button(self, text = str(x)+", "+str(y), command = self.myButtonPressed)
				tempButton.grid(column = x, row = y + 1,padx = 5, pady = 5,ipadx = 5, ipady=5)	


		self.title("My GUI")
		self.mainloop()

	def myButtonPressed(self):
		print("Hello")

if __name__ == '__main__':
	MyGUI()