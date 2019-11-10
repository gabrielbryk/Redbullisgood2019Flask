from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from quantapp import QuantConnector
import json
import logging

SERVER_PORT = 6543
SERVER_HOST = "0.0.0.0"
API_MODE = "GET"


def api_request(request):

    if 'request' not in request.GET and 'request' not in request.POST:
        return Response("Invalid Request")

    req = request[API_MODE]['request']

    if req == "strategies":
        return Response(json.dumps(QuantConnector.getStrategies()))

    if req == "strategy":
        algoID = request.GET['algoID']
        backtestID = request.GET['backtestID']

        data = QuantConnector.getReport(algoID, backtestID)

        return Response(json.dumps(data))

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

