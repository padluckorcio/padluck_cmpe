ATMMachineDataBasemalupet = [
    {
        "Name": {"LastName": "Uhhlol", "FirstName": "Sanmolalagay"},
        "AccountNo": 132607,
        "PIN": 2007,
        "ControlNo": 666,
        "Balance": 9999.99
    },
    {
        "Name": {"LastName": "King", "FirstName": "Yes"},
        "AccountNo": 123123,
        "PIN": 1234,
        "ControlNo": 999,
        "Balance": 0000.00
    },
    {
        "Name": {"LastName": "Oreo", "FirstName": "Kandadu"},
        "AccountNo": 167897,
        "PIN": 3332,
        "ControlNo": 333,
        "Balance": 0000.50
    }
]

myName = input("Enter your first name: ")
PIN = int(input("Enter your PIN: "))

found = False

for account in ATMMachineDataBasemalupet:
    if account["Name"]["FirstName"].lower() == myName.lower() and account["PIN"] == PIN:
        print(f"Good Day, {myName}! Your balance is ₱{account['Balance']:.2f}.")
        found = True
        break

if not found:
    print("Invalid name or PIN. Please try again.")