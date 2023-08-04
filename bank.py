from abc import ABC, abstractmethod

class Bank(ABC):
    def __init__(self):
        self.users = []
        self.bank_balance = 0
        self.loan_feature = True
        self.loan_amount = 0

    @abstractmethod
    def create_user_account(self, name, initial_deposit):
        raise NotImplementedError

    def get_bank_balance(self):
        return self.bank_balance

    def get_total_loan_amount(self):
        return self.loan_amount

    def toggle_loan_feature(self, status):
        self.loan_feature = status


class User(ABC):
    def __init__(self, name, initial_deposit):
        self.name = name
        self.balance = initial_deposit
        self.transaction_history = []

    @abstractmethod
    def deposit(self, amount):
        raise NotImplementedError

    @abstractmethod
    def withdraw(self, amount):
        raise NotImplementedError

    @abstractmethod
    def transfer(self, recipient, amount):
        raise NotImplementedError

    def check_balance(self):
        return self.balance

    def take_loan(self):
        if self.bank.loan_feature == False:
            print(f"{self.name}, loans are disabled by the bank.")
            return

        if self.balance * 2 > self.bank.get_total_loan_amount():
            print(self.name,", is eligible for a loan.")
            self.balance *= 2
            self.bank.loan_amount += self.balance
            self.transaction_history.append(f" {self.name} took a loan of BDT. {self.balance} TAKA")
        else:
            print(self.name,", is not eligible for a loan.")

    def view_transaction_history(self):
        print(f"Transaction History for: {self.name}")
        for transaction in self.transaction_history:
            print(transaction)

class BankImplementation(Bank):
    def create_user_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print("{self.name}, initial deposit must be positive.")
            return

        user = UserImplementation(name, initial_deposit, self)
        self.users.append(user)
        self.bank_balance += initial_deposit
        return user


class UserImplementation(User):
    def __init__(self, name, initial_deposit, bank):
        super().__init__(name, initial_deposit)
        self.bank = bank


    def create_user_account(self, name, initial_deposit):
        if initial_deposit < 0:
            print(f"{self.name}, initial deposit must be positive.")
            return

        user = UserImplementation(name, initial_deposit, self)
        self.users.append(user)
        self.bank_balance += initial_deposit
        return user

    def deposit(self, amount):
        if amount <= 0:
            print("{self.name}, deposit amount must be positive.")
            return

        self.balance += amount
        self.transaction_history.append(f"{self.name}, you deposite BDT. {amount} TAKA")

    def withdraw(self, amount):
        if amount <= 0:
            print("{self.name}, withdrawal amount must be positive.")
            return

        if self.balance >= amount:
            self.balance -= amount
            self.transaction_history.append(f"{self.name}, you withdraw BDT. {amount} TAKA")

    def transfer(self, recipient, amount):
        if amount <= 0:
            print("{self.name}, transfer amount must be positive.")
            return

        if self.balance >= amount:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"{self.name}, you have transferred BDT. {amount} TAKA to {recipient.name}")


bank = BankImplementation()

# create bank account
u1 = bank.create_user_account("Sabbir", 900)
u2 = bank.create_user_account("Arif", 700)

# deposite withdraw
u1.deposit(200)
u2.withdraw(300)

# check available balance
print("==========================================================")
print(f"Balance of {u1.name} is BDT. {u1.check_balance()} TAKA")
print("==========================================================\n")
print(f"Balance of {u2.name} is BDT. {u2.check_balance()} TAKA")
print("==========================================================\n")
#transfer balance
u1.transfer(u2, 400)

# transaction history
u1.view_transaction_history()
print("==========================================================\n")
u2.view_transaction_history()
print("==========================================================\n")

# take loan
u1.take_loan()
print("==========================================================\n")
u2.take_loan()
print("==========================================================\n")

# check total bank balance
print(f"Total Bank balance is BDT. {bank.get_bank_balance()} TAKA")

print("==========================================================\n")
# check laon amount
print(f"Total Loan amount is BDT. {bank.get_total_loan_amount()} TAKA")
print("==========================================================\n")
# turn off loan feature
bank.toggle_loan_feature(False)
u2.take_loan()
print("==========================================================\n")
