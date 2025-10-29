#KEY : VALUE
myInfo = {"Name" : "PrinceSantos", "Age" : 23 , "Gender" : "Gay",}
#all in dictionary
print(myInfo)
#specific in dictionary
print(myInfo["Name"])
print(myInfo["Age"])

myInfo["Name"] = "Redcute"
print(myInfo)
#change or add
myInfo.update({"Citizenship": "African"})
print(myInfo)



myInfo = {
    "Name": {
        "FirstName": "Christopher",
        "LastName": "Nolan",
    },
    "Age": 55,
    "Mindblowing Movies": [
        "Interstellar"
        "Oppenheimer",
        "Inception",
        "Tenet",
        "The Prestige"
        "Memento"
    ]
}
print(myInfo)
print(myInfo["Name"]["LastName"])
print(myInfo["Name"])
print(myInfo["Name"]["FirstName"] + " " + myInfo["Name"]["LastName"])
print(myInfo["Mindblowing Movies"][3])