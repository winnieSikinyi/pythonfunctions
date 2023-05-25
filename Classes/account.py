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
