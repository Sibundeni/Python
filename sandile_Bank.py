account = {}
def create_account():
    if not account:
        account_number = int(input("Enter account number: "))
        account_holder = input("Enter your surname and initials: ")
        initial_amount = float(input("Enter initial amount: "))
        account[account_number] = {'account_holder': account_holder, 'balance':initial_amount}
        print(f"Account {account_number} was successfully created")
    else:
        print("Account number is already created")
def access_account_information():
    account_number = int(input("Enter your account number: "))
    if account_number in account:
        print(f"Account number:{account_number}")
        print(f"account holder: {account[account_number]['account_holder']}")
        print(f"Balance:R{account[account_number]['balance']}")
    else:
        print("account doesnt exist")
def deposit():
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter your amount: "))
    if account_number in account and amount > 0:
        account[account_number]['balance'] += amount
        print(f"R{amount} was deposited. New balance is: {account[account_number]['balance']}")
    else:
        print("account number doesnt exist or amount <= 0")
def withdraw():
    account_number = int(input("Enter your account number: "))
    amount = float(input("Enter your amount: "))
    if account_number in account and amount > 0 and account[account_number]['balance'] >= amount:
        account[account_number]['balance'] -= amount
        print(f"R{amount} was withdrawn. New balance is: {account[account_number]['balance']}")
    else:
        print("invalid account number or insufficient funds")
def delete_account():
    account_number = int(input("Enter your account number: "))
    if account_number in account:
        del account[account_number]
        print(f"Account {account_number} was deleted successfully")
    else:
        print("account is not found")
def view_account():
    if not account:
        print("There are no accounts yet")
    else:
        for account_number in account:
            print(f"Account number: {account_number}")
            print(f"Account holder: {account[account_number]['account_holder']}")
            print(f"Balance:R{account[account_number]['balance']}")

while True:
    print("1. create account")
    print("2. Access account information")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Delete account")
    print("6. View all accounts")
    print("7. Exit")

    choice = input("Enter the number according to what you do (1,2,3,4,5,6,7):")

    if choice == "1":
        create_account()
    elif choice == "2":
        access_account_information()
    elif choice == "3":
        deposit()
    elif choice == "4":
        withdraw()
    elif choice == "5":
        delete_account()
    elif choice == "6":
        view_account()
    elif choice == "7":
        print("you are out")
        break
    else:
        print("invalid choice")
