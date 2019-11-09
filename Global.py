import json
from pymongo import MongoClient

# SETS UP A DATABASE CONNECTION

server_config = "/Users/talhatanveer/server.conf"

try:
    with open(server_config) as server_file:
        server = json.load(server_file)

    database = MongoClient(server['host'], server['port'])
except FileNotFoundError as e:
    print("Unable to open file.")
finally:
    pass



