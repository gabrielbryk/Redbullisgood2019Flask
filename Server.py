from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import logging

SERVER_PORT = 6543
SERVER_HOST = "127.0.0.1"


def api_request(request):
    if not request.GET['request']: return Response("")

    req = request.GET['request']

    if req == "strategies":
        return Response("")

    if req == "strategy":
        strategy_id = request.GET['id']
        return Response("")

    return Response("")


def test_request(api):

    return Response("Hello World")

def auth(request):
    logging.debug("Auth Request Recieved")
    logging.info(request.GET['data'])
    return Response(request.POST['data'])

SERVER_ROUTES = [
    ("api", "/api", api_request),
    ("hello", "/", test_request),
    ("auth", "/auth", auth)
]

# START THE SERVER
if __name__ == '__main__':
    logging.basicConfig(filename='server.log', filemode='w', level=logging.DEBUG, format='%(levelname)s - %(message)s')
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

