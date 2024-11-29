from user import User

class Admin:
    def __init__(self):
        self.users = []
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, acc_type):
        user = User(name, email, address, acc_type)
        self.users.append(user)
        print(f"Account created for {name}.")
        print(f"Account number: {user.account_number}")

    def delete_account(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.users.remove(user)
                print(f"Account {account_number} deleted.")
                return
        print("Account does not exist")

    def all_user(self):
        print("All User Accounts:")
        for user in self.users:
            print(f"Name: {user.name}, Account Number: {user.account_number}, Balance: {user.balance}")

    def total_balance(self):
        total_balance = sum(user.balance for user in self.users)
        print(f"Total available balance of the bank: {total_balance}")

    def total_loan_amount(self):
        total_loan = sum(user.loan_count * 500 for user in self.users)  # Assuming each loan is 500
        print(f"Total loan amount: {total_loan}")

    def loan_feature(self, enable):
        self.loan_feature_enabled = enable
        status = "enabled" if enable else "disabled"
        print(f"Loan feature {status}")
