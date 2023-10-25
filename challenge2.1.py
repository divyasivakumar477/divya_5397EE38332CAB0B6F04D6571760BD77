'''Implemnt a class called bankaccount that represents a bank account.The class should have private
attributes for accounnt number , account holder name , and account balance.include methods to
deposit mony,withdraw money,and display the account balance.ensure that the account balance
cannot be accessed directly from outside the class.write a program to create an instance of the
bankaccount class and test the deposit and withdrawal functionality.'''


class BankAccount:

  def _init_(self,account_number,account_holder_name,initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance
    
  def deposit(self,amount):
    if amount > 0:
      self.__account_balance += amount
      print("deposited ₹{}. New Balance : ₹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount.")

  def withdraw(self,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("withdraw ₹{}. New Balance : ₹{}".format(amount,self.__account_balance))
    else:
      print("invalid withdrawal amount or insufficient balance")
      
  def display_balance(self):
    print("account balance for {} (amount #{}): ₹{}".format(self.__account_holder_name, 
         self._account_number, self._account_balance))
account = BankAccount(account_number ="12345678910",
                      account_holder_name ="divya",
                      initial_balance = 5000.0)

account.display_balance()
account.deposit(500.0)
account.withdraw(6000.0)
account.withdraw(200.0)
account.display_balance()
