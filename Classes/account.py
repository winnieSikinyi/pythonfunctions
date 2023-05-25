class Account:
    account_type = "savings"
    def __init__(self,account_number,balance,account_name,interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.intrest_rate = interest_rate
        self.account_name = account_name
    def deposit(self,amount):
        self.balance+=amount
        return f"{self.account_name } has {self.balance}"
        
    def withdraw(self,amount):
      if self.balance >= amount:
            self.balance -= amount
            return f"Withdrawal successful. New balance: {self.balance}"
      else:
            return "Insufficient funds."
 
    def calculate_interest(self, time):
        interest = (self.balance * self.intrest_rate * time) / 100
        return f"Interest for {time} years: {interest}"
    

    # def print_statement(self):
# Add a new method  print_statement which combines both deposits and 
# withdrawals into one list and, using a for loop, prints each transaction in a new 
# line like this
# deposit - 1000
# withdrawal - 500


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0
    def check_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({
            "amount": amount,
            "narration": "deposit"
        })
    def withdrawal(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        self.withdrawals.append({
            "amount": amount,
            "narration": "withdrawal"
        })
    def print_statement(self):
        for transaction in self.deposits + self.withdrawals:
            print(f"{transaction['narration']} - {transaction['amount']}")
    def borrow_loan(self, amount):
        if self.loan_balance > 0:
            raise ValueError("Account has outstanding loan")
        if amount < 100:
            raise ValueError("Loan amount must be more than 100")
        if len(self.deposits) < 10:
            raise ValueError("Customer must make at least 10 deposits")
        if amount > sum(d["amount"] for d in self.deposits) / 3:
            raise ValueError("Loan amount must be less than or equal to 1/3 of total deposits")
        self.loan_balance += amount
    def repay_loan(self, amount):
        if self.loan_balance < amount:
            raise ValueError("Loan amount is more than outstanding loan")
        self.loan_balance -= amount
        self.balance += amount
    def transfer(self, amount, other_account):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount
        other_account.balance += amount
