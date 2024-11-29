from user import User
from admin import Admin

admin = Admin()

while True:
    print("\nWelcome To Our Management System")
    print("1. Admin Panel")
    print("2. User Panel")
    print("3. Exit")

    option = int(input("\nEnter your option: "))
    if option == 1:
        print("\nWelcome To Admin Panel")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See all user accounts list")
        print("4. Check total available balance")
        print("5. Check total loan amount")
        print("6. Toggle loan feature")
        print("7. Exit Admin Panel")

        a = int(input("\nEnter choice: "))
        if a == 1:
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            acc_type = input("Enter account type (Savings/Current): ")
            admin.create_account(name, email, address, acc_type)
        elif a == 2:
            account_number = input("Enter account number to delete: ")
            admin.delete_account(account_number)
        elif a == 3:
            admin.all_user()
        elif a == 4:
            admin.total_balance()
        elif a == 5:
            admin.total_loan_amount()
        elif a == 6:
            enable = input("Enable loan feature? (yes/no): ").lower() == 'yes'
            admin.loan_feature(enable)
        elif a == 7:
            continue
        else:
            print("Please choose a valid option")

    elif option == 2:
        print("\nWelcome To User Panel")
        print("1. Deposit")
        print("2. Withdrawal")
        print("3. Check balance")
        print("4. Check transaction history")
        print("5. Take loan")
        print("6. Fund Transfer")
        print("7. Exit User Panel")

        b = int(input("\nEnter your choice: "))
        if b == 1:
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to deposit: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.deposit(amount)
                    break
            else:
                print("Account does not exist")
        elif b == 2:
            account_number = input("Enter your account number: ")
            amount = float(input("Enter amount to withdraw: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.withdrawal(amount)
                    break
            else:
                print("Account does not exist")
        elif b == 3:
            account_number = input("Enter your account number: ")
            for user in admin.users:
                if user.account_number == account_number:
                    user.check_balance()
                    break
            else:
                print("Account does not exist")
        elif b == 4:
            account_number = input("Enter your account number: ")
            for user in admin.users:
                if user.account_number == account_number:
                    user.check_transaction_history()
                    break
            else:
                print("Account does not exist")
        elif b == 5:
            account_number = input("Enter your account number: ")
            amount = float(input("Enter loan amount: "))
            for user in admin.users:
                if user.account_number == account_number:
                    user.take_loan(amount)
                    break
            else:
                print("Account does not exist")
        elif b == 6:
            account_number = input("Enter your account number: ")
            recipient_account_number = input("Enter recipient account number: ")
            amount = float(input("Enter amount to transfer: "))
            recipient = None
            for user in admin.users:
                if user.account_number == recipient_account_number:
                    recipient = user
                    break
            for user in admin.users:
                if user.account_number == account_number:
                    user.fund_transfer(amount, recipient)
                    break
            else:
                print("Account does not exist")
        elif b == 7:
            continue
        else:
            print("Please choose a valid option")

    elif option == 3:
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Please choose 1, 2, or 3")
