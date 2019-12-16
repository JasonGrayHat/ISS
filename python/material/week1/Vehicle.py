class Vehicle:
	'''
	Author: Jordan Doerksen
	Class: Vehicle
	Abstract: This class defines a vehicle for a dealership

	Mod Date: 2019/11/26
	'''
	def __init__(self,year = 9999,numberOfPass = 9999,make = "N/A",model = "N/A",color = "N/A",milage = -1,price = 0,cost = 0):
		self.year = year
		self.numberOfPass = numberOfPass
		self.make = make
		self.model = model
		self.color = color
		self.milage = milage
		self.price = price
		self.cost = cost
		self.vin = "DEFAULT"

	def getMarkUp(self):
		return self.price - self.cost
