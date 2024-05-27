class Account:
    def __init__(self,number,pin,owner_name,overdraft) :
        self.owner_name=owner_name
        self.number=number
        self.__pin = pin
        self.overdraft=overdraft
        self.__balance=0
        self.is_frozen= False
        
        
    def show_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        else:return "wrong pin"
        
        
    def view_account_details(self,owner_name):
        if owner_name == self.owner_name:
            print(f"Account owner {self.owner_name} has a current balance of {self.__balance}")
        else:
            print("owner name does not exist please input correct name.")
    
    
    def change_account_owner(self, new_owner_name, new_pin,new_number):
       print(f"{new_owner_name} is the new owner to account number {self.number} with pin {new_pin} is the owner of account  {new_number}")
       
       
    def account_statement(self,pin):
        if self.__pin==pin:
            print(f"{self.owner_name} you have youre account balance is {self.__balance}")
            
            
    def overdraft_limit(self, new_overdraft_limit):
        self.overdraft = new_overdraft_limit  
        print(f"{self.owner_name} your overdraft limit is Ksh {self.overdraft}")
        
        
    def intrest_calulation(self,intrest_rate):
        intrest =self.__balance*intrest_rate
        print(intrest)
        
        
    def freeze_account(self):
        if self.is_frozen == True:
            print(f"{self.owner_name} your account has been frozen")
            
        else:
            print("continue your accont is notfrozen ")
            

class BankAccount:
    def __init__(self, name, account_number, salary,min_balance,balance):
        self.name = name
        self.account_number = account_number
        self.salary = salary
        self.balance=balance
        self.min_balance=min_balance
        self.transactions = []

    def description(self):
        print("Name is: ", self.name)
        print("Account Number is: ", self.account_number)
        print("Salary is: ", self.salary)

    def deposit(self, deposit):
        acc1=self.salary + deposit
        self.transactions.append({"type": "deposit", "amount": deposit})
        print(acc1)
        
        self.transactions.append({"type": "deposit", "amount": deposit})
        print(acc1)
        
        
    def withdraw(self, withdraw):
        if self.salary - withdraw >= 0:
            self.salary -= withdraw
            self.transactions.append({"type": "withdrawal", "amount": withdraw})
        else:
            print("Insufficient funds")

    def withdraw(self, withdraw):
        if self.salary - withdraw >= 0:
            self.salary -= withdraw
            self.transactions.append({"type": "withdrawal", "amount": withdraw})
        else:
            print("Insufficient funds")


    def transaction_history(self):
        for transaction in self.transactions:
            if transaction["type"] == "deposit":
                print(f"Deposited: ${transaction['amount']}")
            elif transaction["type"] == "withdrawal":
                print(f"Withdrew: ${transaction['amount']}")   
       
                
    def minimum_balance(self):
        self.min_balance==10000
        print(f"{self.name} you're minimum balance is {self.min_balance}")
 
    
    def transfer_fund(self,transfered_amount,receiver) :
        if self.balance - transfered_amount>=0:
            self.balance -= transfered_amount
            print(f"{self.name} tramsfered {transfered_amount} to {receiver} ")  
        else:
            print("Insuficient funds") 
            
    def close_account(self):
        print(f"Account number {self.account_number} has been closed.")
        
        
            


        
        
         

        
        
        
            
          
               
        
    