from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def auth(request):
  print(request.GET['data'] )
  return Response(request.GET['data'])
   


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('auth', '/auth')
        config.add_view(auth, route_name='auth')
        app = config.make_wsgi_app()
    server = make_server('127.0.0.1', 8080, app)
    server.serve_forever()