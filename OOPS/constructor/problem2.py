class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo
        
    # debit
    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} is debited!")
        print(f"net balance = {self.get_balance()}")
    
      
    # credit 
    def credit(self, amount):
        self.balance += amount
        print(f"RS. {amount} is credited!")
        print(f"net balance = {self.get_balance()}")
        
        
    def get_balance(self):
        return self.balance
    
cust1 = Account(10000, 12345)
cust1.debit(1000)
cust1.credit(1500)
        