from hashpass import hash_password
import getpass

def login(client_list: "ClientsNotebook"):
    attemps = 0
    while attemps < 3:
        username_input = input("username: ")
        password_input = getpass.getpass("pasword: ")
        password_input = hash_password(password_input)
        # if client gest and {} that means that there's no client
        client = client_list.get_client(username_input)

        if client and client["password"] == password_input:
            print("logged")
            return True
        else:
            print("credentials wronggg")
            attemps += 1
    print("bye! ;)")
    exit()

