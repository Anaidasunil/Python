class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: {self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Added interest {interest}. New balance is {self.balance}.")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0:
            if self.balance + self.overdraft_limit >= amount:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance is {self.balance}.")
            else:
                print("Overdraft limit exceeded.")
        else:
            print("Withdrawal amount must be positive.")


def main():
    savings = SavingsAccount("SA12345", "Ann", 1000)
    checking = CheckingAccount("CA12345", "Binoy", 500)

    print(savings)
    savings.deposit(200)
    savings.add_interest()
    savings.withdraw(500)
    print(savings)

    print(checking)
    checking.deposit(300)
    checking.withdraw(1000)
    checking.withdraw(200)
    print(checking)


if __name__ == "__main__":
    main()
