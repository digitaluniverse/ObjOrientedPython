import statistics

class Score:
	
	def __init__(self, list):
		list.sort()
		self.list = list
		self.length = len(list)
	
	def mean(self):
		list = self.list
		sum = 0
		for x in list:
			sum = sum + x
		mean = sum / len(list)
		return mean
		
	def standardDeviation(self):
		list = self.list
		stdiv = statistics.stdev(list)
		return stdiv
		
	def highestScore(self):
		list = self.list
		return list[self.length-1]
		
	def lowestScore(self):
		list = self.list
		return list[0]
		