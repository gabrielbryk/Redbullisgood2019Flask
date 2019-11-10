from pymongo import MongoClient
import time

class Transaction:

    def __init__(self):
        password = input("Enter database password: ")
        self.dbclient = MongoClient("mongodb+srv://admin:"+password+"@strategycloud-zlvrl.gcp.mongodb.net/test?retryWrites=true&w=majority")
        self.database = self.dbclient['strategycloud']

    def make_new_transaction(self, username, amount):
        balance = self.getUserBalance(username)['balance']
        new_balance = int(balance) + int(amount)

        self.database['users'].update({"username":username},{"$set":{"wallet":new_balance}})

        # LOG THIS TRANSACTION
        transaction_id = self.log_transaction(username, int(amount), int(new_balance), time.time())['transaction_id']

        return {'balance':new_balance,'transaction_id':transaction_id}

    def log_transaction(self, username, amount, balance, timestamp):

        transaction_id = self.database['transactions'].insert({"username":username,"amount":amount,"balance":balance, "timestamp":timestamp})
        return {'transaction_id':str(transaction_id)}

    def get_transaction_history(self, username):
        cursor = self.database['transactions'].find({'username':username})
        transactions = []
        for t in cursor:
            t['_id'] = str(t['_id'])
            transactions.append(t)

        return transactions

    def getUserBalance(self, username):
        users = self.database['users']
        data = users.find_one({'username':username})
        return {'balance':data['wallet']}