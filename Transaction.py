from pymongo import MongoClient

class Transaction:

    def __init__(self):
        password = input("Enter database password: ")
        self.dbclient = MongoClient("mongodb+srv://admin:"+password+"@strategycloud-zlvrl.gcp.mongodb.net/test?retryWrites=true&w=majority")
        self.database = self.dbclient['strategycloud']

    def make_new_transaction(self, username, amount):
        balance = self.getUserBalance(username)
        new_balance = int(balance) - int(amount)

        pass

    def getUserBalance(self, username):
        users = self.database['users']
        data = users.find_one({'username':username})
        return data['wallet']