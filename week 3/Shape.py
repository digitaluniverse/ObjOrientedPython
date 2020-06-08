import math

class Shape:
	
	def __init__(self, centerX, centerY, color):
		self.centerX = centerX
		self.centerY = centerY
		self.color = color
		
	def getX(self):
		centerX = self.centerX
		return centerX

	def getY(self):
		centerY = self.centerX
		return centerY

	def move(self,x,y):
		self.centerX = x
		self.centerY = y

	def setColor(self,color):
		self.color = color

class Circle(Shape):
	
	def __init__(self, centerX, centerY, color, radius):
		super().__init__(centerX, centerY, color)
		self.radius = radius
	
	def getArea(self):
		radius = self.radius
		area = math.pi * radius ** 2
		return area
	
	def getPerimeter(self):
		radius = self.radius
		perimeter = math.pi * radius * 2 
		return perimeter
	
class Rectangle(Shape):
	
	def __init__(self, centerX, centerY, color, width, height):
		super().__init__(centerX, centerY,color)
		self.width = width
		self.height = height
	
	def getArea(self):
		width = self.width
		height = self.height
		area = width*height
		return area
	
	def getPerimeter(self):
		width = self.width
		height = self.height
		perimeter = 2 * width + 2* height
		return perimeter
	
class Triangle(Shape):

	def __init__(self, centerX, centerY, color, side1, side2, side3):
		super().__init__(centerX, centerY,color)
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3

	def getArea(self):
		side1 = self.side1
		side2 = self.side2
		side3 = self.side3
		s = (side1 + side2 + side3) / 2	
		area = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
		return area

	def getPerimeter(self):
		side1 = self.side1
		side2 = self.side2
		side3 = self.side3
		perimeter = side1 + side2 + side3
		return perimeter