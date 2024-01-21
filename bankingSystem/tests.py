import unittest
from clients_notebook import ClientsNotebook
from hashpass import hash_password

class TestClientsCsv(unittest.TestCase):
    def test_get_client(self):
        clients = ClientsNotebook()
        admin = clients.get_client("admin")
        self.assertEqual(admin["name"], "admin")

class TestHashPasswords(unittest.TestCase):
    def test_hash_pass(self):
       hashed = hash_password("adminpass") 
       hashed2 = hash_password("danpass")
       self.assertEqual(hashed, "713bfda78870bf9d1b261f565286f85e97ee614efe5f0faf7c34e7ca4f65baca")
       self.assertEqual(hashed2, "3fefe67eacddf6534149c2a8989bfa07a0ff7e194208ca7a88c411a1264ad863")

if __name__ == "__main__":
    unittest.main()
