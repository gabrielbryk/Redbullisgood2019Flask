from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

SERVER_PORT = 6543
SERVER_HOST = "0.0.0.0"


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


SERVER_ROUTES = {
    ["api", "/api", api_request],
    ["hello", "/", test_request]
}

# START THE SERVER
if __name__ == '__main__':
    with Configurator() as config:
        for route, path, method in SERVER_ROUTES:
            config.add_route(route, path)
            config.add_view(method, route_name=route)

        app = config.make_wsgi_app()

    print("Starting Server...")
    server = make_server(SERVER_PORT, SERVER_PORT, app)
    print("Server Running on "+SERVER_HOST+":"+str(SERVER_PORT))
    server.serve_forever()

