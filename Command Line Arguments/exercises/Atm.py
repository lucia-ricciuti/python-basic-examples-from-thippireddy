import sys

commands = sys.argv

accountBalance = 10000

command = commands[1]
# Check
if command == "1":
    print(f"The account balance is: {accountBalance:.2f}.")
# Withdraw
elif command == "2":
    amount = float(input("How much you want to withdraw? "))
    accountBalance -= amount
    print(f"Withdrawn: {amount:.2f}")
    print(f"Updated account balance is: {accountBalance:.2f}.")
# Deposit Cash
elif command == "3":
    amount = float(input("How much cash you want to deposit? "))
    accountBalance += amount
    print(f"Deposited cash: {amount:.2f}")
    print(f"Updated account balance is: {accountBalance:.2f}.")
# Deposit Check
elif command == "4":
    amount = float(input("How much is the check you want to deposit? "))
    accountBalance += amount
    print(f"Deposited check: {amount:.2f}")
    print(f"Updated account balance is: {accountBalance:.2f}.")
else: 
    print("Command not recognized: "+command)
    
        