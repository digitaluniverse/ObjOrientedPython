class Rational:

	def __init__(self,numerator,denominator):
		gcd = self.greatest(numerator,denominator)
		self.numerator = numerator // gcd
		self.denominator = denominator // gcd

	def greatest(self,a,b):
		if b == 0:
			return a
		return self.greatest(b, (a % b))

	def __add__(self, other):
		numerator = self.numerator + other.denominator + self.denominator * other.denominator
		denominator = self.denominator + other.denominator
		return Rational(numerator, denominator)

	def __sub__(self, other):
		commDom = self.denominator * other.denominator
		one =  self.numerator * other.denominator
		two = other.numerator * self.denominator
		difference = one - two
		return Rational(difference, commDom)

	def __mul__(self, other):
		one = self.numerator * other.numerator
		two = self.denominator * other.denominator
		return Rational(one, two)

	def __div__(self, other):
		one = self.numerator * other.denominator
		two = self.denominator * other.numerator
		return Rational(one, two)

	def __str__(self):
		return '{self.numerator}/{self.denominator}'.format(self=self)

