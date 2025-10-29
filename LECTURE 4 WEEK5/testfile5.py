

isPresent = False
isExist = True

isAvailable = "True"

isValid = 1
isOkay = 0

isNumeric = False
Char = "20"

isNumeric = Char.isnumeric()
strIsNumeric = str(Char.isnumeric())
print((isNumeric))
print((strIsNumeric))

#AND, OR, NOT-----




a = 4001
b = 5001
isEE = (a == b)
print((isEE))
isGTE= (a >= b)
print((isGTE))
isLTE = (a <= b)
print((isLTE))

#membership and identity operator
#in, not in is, is not

isIn = (10 in [20, 40, 60, 10 ,30])
print((isIn)) #True
isIn = (10 in [20, 40, 60, 5 ,30])
print((isIn)) #False

isIn = ("andrei" in "andrei rj red")
print(isIn)

isIs = ("jhonray" == "Jhonray")
print(isIs)
isIs = ("jhonray" == "red andrei")
print(isIs)

#logical operator

isOkay = (10 in [20, 40, 60, 10 ,30] and (10 in [20, 40, 60, 5 ,30]))
print(isOkay)

isIn = ("andrei kiss si jhonrey " in "andrei kiss si jhonrey inggit si red")
print(isIn) #True daw