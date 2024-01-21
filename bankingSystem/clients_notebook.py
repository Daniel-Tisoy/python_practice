import csv

# ----------------section manage client list -------------------

class ClientsNotebook:
    def __init__(self):
        #client data stored in csv
        #name - password - balance
        self.clients_list = list()
        with open("clients.csv", "r") as f_clients:
            reader = csv.DictReader(f_clients)
            for row in reader:
                self.clients_list.append(row)

    # search data in clients list
    def get_client(self, username: str) -> dict:
        for client in self.clients_list:
            if client["name"] == username:
                return client 
        return {} 
