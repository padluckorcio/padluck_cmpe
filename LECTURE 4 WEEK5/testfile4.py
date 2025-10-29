#Numerical integer (-3,0,562) float (23.23252) complex number (45 + 25i)
#i = ampere, j = imaginary resistance 25 + j25 = impedance

myIntegerA = 60
myIntegerB = 30
myIntegerC = 6
myFloatA = 25.45
myFloatB = 14.45
myComplexA = 25 - 3j
myComplexB = 10 + 3j

#+,-,/, *,
import math

sum = myIntegerA + myIntegerB
print(sum)
difference = myIntegerA - myIntegerB * myIntegerC
print(difference)

exponent = 2 ** 3
print(exponent)

product= myIntegerA * myIntegerB + myIntegerA * myIntegerC
print(product)

quotient = myIntegerA / myIntegerB
print(quotient)
Roundqoutient = round(quotient, 2)
print(Roundqoutient)

remainder = myIntegerA % myIntegerC
print(remainder)

remainder = myIntegerB % myIntegerB
print(remainder)

#Parenthesis,Exponent,Multiplication,Division,Addition,Subtraction
myComProduct = myComplexA * myComplexB
print(myComProduct)

print(5*4*2*2*1)
print(math.factorial(5))

cos_90_deg = math.cos(math.radians(60))
print(cos_90_deg)


