import Rational

fractionOne = Rational.Rational(2,6)
fractionTwo = Rational.Rational(6,10)

print("Reduced form of Fraction One: {}".format(fractionOne))
print("Reduced form of Fraction Two: {}".format(fractionTwo))

print("Addition {} + {} = {} ".format(fractionOne,fractionTwo,fractionOne.__add__(fractionTwo)))
print("Subtraction {} - {} = {} ".format(fractionOne,fractionTwo,fractionOne.__sub__(fractionTwo)))
print("Multiplication {} x {} = {} ".format(fractionOne,fractionTwo,fractionOne.__mul__(fractionTwo)))
print("Division {} ÷ {} = {} ".format(fractionOne,fractionTwo,fractionOne.__div__(fractionTwo)))
