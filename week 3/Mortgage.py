class Mortgage:
	
	def __init__(self, rate, amount, time):
		self.rate = rate
		self.amount = amount
		self.time = time
	
	def monthly(self):
		rate = self.rate / 100 / 12
		amount = self.amount
		time = self.time * 12
		monthlyAmount = amount * ((rate * ((1+rate) ** time)) / ((1+rate) ** time - 1))
		return monthlyAmount
	
	def total(self):
		rate = self.rate / 100
		amount = self.amount
		time = self.time
		total = amount * ((rate * ((1+rate) ** time)) / ((1+rate) ** time - 1)) * time
		return total