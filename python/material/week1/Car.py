from Vehicle import Vehicle

class Car(Vehicle):
	'''
	'''
	def __init__(self,year = 9999,numberOfPass = 9999,make = "N/A",model = "N/A",color = "N/A",milage = -1,price = 0,cost = 0,body = "N/A",numberOfWheels = 0,engineType = "N/A",HP = 0,feature = []):
		super().__init__(year,numberOfPass,make,model,color,milage,price,cost)
		self.body = body
		self.numberOfWheels = numberOfWheels
		self.engineType = engineType
		self.HP = HP
		self.feature = feature
