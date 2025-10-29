from time import process_time

strFullName = ("Padluck Orcio")

strNewValue = strFullName.upper()
print(strNewValue)

strNewValue = strFullName.count("u")
print(strNewValue)

strNewValue = strFullName.split(" ")
print(strNewValue)

#replace
strNewValue = strFullName.replace("Padluck", "Kandadu")
print(strNewValue)

#join
strFirstName = ("Padluck")
StrMiddleName = ("Soliman")
strLastName = ("Orcio")
strFullName = "_".join((strFirstName, StrMiddleName, strLastName))
print(strFullName)

NewValue = strFullName.isnumeric()
print(strNewValue)

NewValue = strFullName[2:7]
print(NewValue)#substring
NewValue = strFullName[2:7:3]
print(NewValue) #substring with jump
#return the lowest index
print(strFullName.index("u"))
print(strFullName.index("u",2,7))


strInput = "123andrei123 red"
print(strInput.replace("andrei123", "kain daga"))

newString = "kain daga"
for char in strInput:
    if not char.isdigit():
        newString = newString + char

print(newString)

strInput = "12323121321321321313daga"
newString = " "
for char in strInput:
    if not char.isnumeric():
