from pymongo import MongoClient


class Transaction:

    def __init__(self):
        self.dbclient = MongoClient()

    def make_new_transaction(self, username, amount):
        pass