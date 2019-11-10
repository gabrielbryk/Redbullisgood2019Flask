from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from quantapp import QuantConnector
from Transaction import Transaction
from Notification import Notification
import json
import logging

SERVER_PORT = 6543
SERVER_HOST = "0.0.0.0"

QuantAPI = QuantConnector()
TransactionAPI = Transaction()
NotificationAPI = Notification()

def authenticate(token):
    return True


def api_request(request):
    global QuantAPI

    # CHECK IF PARAMS ARE SET
    if 'request' not in request.GET:
        return Response("Invalid Request")

    req = request.GET['request']

    try:
        if req == "strategies":
            strategies = QuantAPI.getStrategies()

            new_data = []
            for strategy in strategies:
                stats = QuantAPI.basicStats(strategy['algorithm_id'], strategy['backtest_id'])
                strategy['stats'] = stats
                new_data.append(strategy)

            return Response(json.dumps(new_data))

        if req == "strategy":
            algoID = request.GET['algoID']
            backtestID = request.GET['backtestID']

            return Response(json.dumps(QuantAPI.getReport(algoID,backtestID)))

        if req == "invest":
            amount = float(request.GET['amount'])
            algoID = request.GET['algoID']
            backtestID = request.GET['backtestID']
            username = request.GET['username']

            result = QuantAPI.percentReturn( algoID, backtestID, amount)['net']
            transaction = TransactionAPI.make_new_transaction( username, result )

            transaction_message = "Your transaction (#A33121) has been completed with a net return of $"+str(result)+"."
            NotificationAPI.send_sms(transaction_message, "+13123940768")

            return Response(json.dumps(transaction))

        if req == "user_balance":
            balance = TransactionAPI.getUserBalance(request.GET['username'])

            return Response(json.dumps(balance))

        if req == "transaction":
            username = request.GET['username']
            amount = request.GET['amount']

            transaction = TransactionAPI.make_new_transaction(username, amount)

            return Response(json.dumps(transaction))

        if req == "strategy_stats":

            return Response("")

    except Exception as e:
        return Response("Error while processing your request "+str(e))
    finally:
        pass

    return Response("")


SERVER_ROUTES = [
    ("api", "/api", api_request)
]

# START THE SERVER
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
    logging.debug("Configuring Server...")
    with Configurator() as config:
        for route, path, method in SERVER_ROUTES:
            config.add_route(route, path)
            config.add_view(method, route_name=route)

        app = config.make_wsgi_app()

    logging.debug("Starting Server...")
    server = make_server(SERVER_HOST, SERVER_PORT, app)
    logging.debug("Server Running on "+SERVER_HOST+":"+str(SERVER_PORT))
    server.serve_forever()

