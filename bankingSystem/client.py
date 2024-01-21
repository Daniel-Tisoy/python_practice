
# client is a person how has data in the csv file
# client class is used to perform the requirements in readme.md
class Client:

  def __init__(self, username: str, balance: int = 2000):
    self.username = username
    self.balance = balance 

  def deposit(self, amount: int):
    self.balance += amount
    print(f"\nDeposited ${amount}. New balance: ${self.balance}")

  def withdraw(self, amount: int):
    if amount > self.balance:
        print("\ninsuficent founds :(")
    else:
        self.balance -= amount
        print(f"\nWithdrawn ${amount}. New balance: ${self.balance}")

  def __str__(self):
    return (f"Username: {self.username} \nBalance: ${self.balance}")

  def transfer(self, client: 'Client', amount: int):
    if amount > self.balance:
      print("Insufficient funds")
    else:
      print(f"{self.username}:")
      self.withdraw(amount)
      print(f"{client.username}:")
      client.deposit(amount)
      print("Transfer successful")



