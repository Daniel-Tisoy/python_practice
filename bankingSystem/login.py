from hashpass import hash_password
import getpass

def login(client_list: "ClientsNotebook") -> dict:

  """
  return a dict with {name: clientname, password: hash, balance: integer}
  the result returned will be used as a client session
  """
  attemps = 0
  while attemps < 3:
    username_input = input("username: ")
    password_input = getpass.getpass("pasword: ")
    password_input = hash_password(password_input)
    # if client gest and {} that means that there's no client
    client = client_list.get_client(username_input)

    if client and client["password"] == password_input:
      print("logged")
      return client 
    else:
      print("credentials wronggg")
      attemps += 1
  print("bye! ;)")
  # If the user enters the wrong credentials three times, the system must lock them out.
  exit()

