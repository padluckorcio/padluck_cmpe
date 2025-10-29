##ATM
#list of a nested dict
ATMMachineDataBasemalupet = [
    { "Name": {
        "LastName": "Uhhlol",
        "FirstName": "Sanmolalagay", }
        ,
    "AccountNo": 132607,
    "PIN" :2007  ,
    "ControlNo" : 666,
    "Balance" : 9999.99
    } ,
{ "Name": {
        "LastName": "King",
        "FirstName": "Yes", }
        ,
    "AccountNo": 123123,
    "PIN" :1234  ,
    "ControlNo" : 999,
    "Balance" : 0000.00
    } ,
{ "Name": {
        "LastName": "Oreo",
        "FirstName": "Kandadu", }
        ,
    "AccountNo": 171717,
    "PIN" :3332  ,
    "ControlNo" : 333,
"Balance" : 0000.50
    } ,
    ]
myName = input("Enter your name: ")
PIN = input("Enter your PIN: ")
Balance = float(input("Enter your balance: "))  # convert input to number

print(f"Good Day! {myName}! Your balance is {Balance}")