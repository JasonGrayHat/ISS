from tkinter import *
from tkinter import messagebox
from tkinter import font

class Calculator(Tk):
	'''
	'''
	def __init__(self):
		super().__init__()
		self.title("Calculator")
		self.font = font.Font(family='Times', size=38, weight='bold')
		px = 2
		py = 2
		ipx = 2
		ipy = 2

		self.txt_input = Entry(self, font = self.font)
		self.txt_input.grid(row = 0, column = 0, columnspan = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_equal = Button(self, text = "=", font = self.font)
		self.btn_equal.grid(row = 0, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_1 = Button(self,text = "1",font = self.font, command = self.btn_1Action)
		self.btn_1.grid(row = 1, column = 0,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_2 = Button(self,text = "2",font = self.font, command = self.btn_2Action)
		self.btn_2.grid(row = 1, column = 1,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_3 = Button(self,text = "3",font = self.font, command = self.btn_3Action)
		self.btn_3.grid(row = 1, column = 2,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_4 = Button(self,text = "4",font = self.font, command = self.btn_4Action)
		self.btn_4.grid(row = 2, column = 0,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_5 = Button(self,text = "5",font = self.font, command = self.btn_5Action)
		self.btn_5.grid(row = 2, column = 1,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_6 = Button(self,text = "6",font = self.font, command = self.btn_6Action)
		self.btn_6.grid(row = 2, column = 2,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_7 = Button(self,text = "7",font = self.font, command = self.btn_7Action)
		self.btn_7.grid(row = 3, column = 0,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_8 = Button(self,text = "8",font = self.font, command = self.btn_8Action)
		self.btn_8.grid(row = 3, column = 1,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_9 = Button(self,text = "9",font = self.font, command = self.btn_9Action)
		self.btn_9.grid(row = 3, column = 2,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_sign = Button(self, text = "+/-", font = self.font)
		self.btn_sign.grid(row = 4, column = 0,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_0 = Button(self, text = "0", font = self.font, command = self.btn_0Action)
		self.btn_0.grid(row = 4, column = 1,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_dot = Button(self, text = ".", font = self.font, command = self.btn_dotAction)
		self.btn_dot.grid(row = 4, column = 2,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_divide = Button(self, text = "%", font = self.font, command = self.btn_divideAction)
		self.btn_divide.grid(row = 1, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_multiply = Button(self, text = "x", font = self.font, command = self.btn_multiplyAction)
		self.btn_multiply.grid(row = 2, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_minus = Button(self, text = "-", font = self.font, command = self.btn_minusAction)
		self.btn_minus.grid(row = 3, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.btn_plus = Button(self, text = "+", font = self.font, command = self.btn_plusAction)
		self.btn_plus.grid(row = 4, column = 3,padx = px,pady = py,ipadx = ipx,ipady = ipy,sticky = "NESW")

		self.grid_columnconfigure(0, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.grid_columnconfigure(2, weight=1)
		self.grid_columnconfigure(3, weight=1)

		self.grid_rowconfigure(0, weight = 1)
		self.grid_rowconfigure(1, weight = 1)
		self.grid_rowconfigure(2, weight = 1)
		self.grid_rowconfigure(3, weight = 1)

		self.mainloop()

	def btn_1Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"1")
	def btn_2Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"2")
	def btn_3Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"3")
	def btn_4Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"4")
	def btn_5Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"5")
	def btn_6Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"6")
	def btn_7Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"7")
	def btn_8Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"8")
	def btn_9Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"9")
	def btn_0Action(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"0")
	def btn_dotAction(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+".")
	def btn_divideAction(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"%")
	def btn_multiplyAction(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"x")
	def btn_minusAction(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"-")
	def btn_plusAction(self):
		tempText = self.txt_input.get()
		self.txt_input.delete(0,END)
		self.txt_input.insert(END, tempText+"+") 

if __name__ == '__main__':
	Calculator()