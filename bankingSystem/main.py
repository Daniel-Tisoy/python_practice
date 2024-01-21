# get the passwords in tests.py 

import login
from clients_notebook import ClientsNotebook
from client import Client


def transfer_to_client(client_list: "ClientNotebook",submiter: "Client", user_receiver: str, amount: int): 
  # get the user in the users list if exists
  exist_receiver= client_list.get_client(user_receiver)

  # submiter can't transfer to himself
  if exist_receiver and submiter.username != exist_receiver["name"]:
    #get client methods
    receiver = Client(exist_receiver["name"], int(exist_receiver["balance"]))
    submiter.transfer(receiver, amount)  
  else:
      print("the client doesn't exist")


# Main program loop
def main():
  # get the records from the csv file
  clients_list = ClientsNotebook()

  # here: after three attemps the program will finish
  user_loged = login.login(clients_list)
  
  # get client methods -> deposit, view, etc..
  user_client = Client(user_loged["name"], int(user_loged["balance"]))

  menu = "1. Deposit\n2. Withdraw\n3. View\n4. Transfer\n5. Exit"

  while True:
    
    print(menu)

    choice = input("Enter your choice: ")
    if choice == "1":
      amount = int(input("Enter the amount to deposit: "))
      user_client.deposit(amount)
    elif choice == "2":
      amount = int(input("Enter the amount to withdraw: "))
      user_client.withdraw(amount)
    elif choice == "3":
      # just using the __str__ method
      print(user_client) 

    elif choice == "4":
      username = input("Enter the username of the recipient: ")
      amount = int(input("Enter the amount to transfer: "))

      transfer_to_client(clients_list, user_client, username, amount)
    elif choice == "5":
      print("Exiting...")
      break

if __name__ == "__main__":
    main()
