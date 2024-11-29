import random

class User:
    def __init__(self, name, email, address, acc_type):
        self.name = name
        self.email = email
        self.address = address
        self.acc_type = acc_type
        self.balance = 0
        self.account_number = self.generate_account_number()
        self.transaction_history = []
        self.loan_count = 0

    def generate_account_number(self):
        return str(random.randint(100000, 999999))

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: {amount}")
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Available balance: {self.balance}")

    def check_transaction_history(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)

    def take_loan(self, amount):
        if self.loan_count < 2:
            self.balance += amount
            self.loan_count += 1
            self.transaction_history.append(f"Loan taken: {amount}")
            print(f"Loan of {amount} taken. New balance: {self.balance}")
        else:
            print("Loan limit exceeded")

    def fund_transfer(self, amount, recipient):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
        elif recipient is None:
            print("Account does not exist")
        else:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
            recipient.transaction_history.append(f"Received: {amount} from {self.name}")
            print(f"Transferred {amount} to {recipient.name}. New balance: {self.balance}")
