from bank import Bank

bank = Bank()

while True:

    print("\n====== BANKING SYSTEM ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        username = input("Enter username: ")
        pin = input("Enter 4-digit PIN: ")

        if username == "" or pin == "":
            print("Fields cannot be empty")
            continue

        print(bank.create_account(username, pin))

    elif choice == "2":

        username = input("Enter username: ")
        pin = input("Enter PIN: ")

        success, message = bank.login(username, pin)

        if success:

            print("\nLogin Successful")

            while True:

                print("\n------ MENU ------")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Balance Enquiry")
                print("4. Mini Statement")
                print("5. Logout")

                option = input("Enter option: ")

                if option == "1":

                    try:
                        amount = float(input("Enter amount: "))

                        if amount <= 0:
                            print("Amount must be positive")
                            continue

                        bank.deposit(username, amount)

                        print("Amount deposited successfully")

                    except ValueError:
                        print("Invalid amount")

                elif option == "2":

                    try:
                        amount = float(input("Enter amount: "))

                        if amount <= 0:
                            print("Amount must be positive")
                            continue

                        if bank.withdraw(username, amount):
                            print("Amount withdrawn successfully")

                        else:
                            print("Insufficient balance")

                    except ValueError:
                        print("Invalid amount")

                elif option == "3":

                    balance = bank.get_balance(username)

                    print(f"Current Balance: ₹{balance}")

                elif option == "4":

                    history = bank.get_history(username)

                    print("\n----- MINI STATEMENT -----")

                    if len(history) == 0:
                        print("No transactions found")

                    else:
                        for item in history:
                            print(item)

                elif option == "5":

                    print("Logged out successfully")
                    break

                else:
                    print("Invalid option")

        else:
            print(message)

    elif choice == "3":

        print("Thank you for using Banking System")
        break

    else:
        print("Invalid choice")
