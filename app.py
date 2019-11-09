from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import logging


def auth(request):
  print(request.GET['data'] )
  return Response(request.POST['data'])
   


if __name__ == '__main__':
  logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
  with Configurator() as config:
      config.add_route('auth', '/auth')
      config.add_view(auth, route_name='auth')
      app = config.make_wsgi_app()
  server = make_server('127.0.0.1', 8080, app)
  logging.info("Server Loaded")

  server.serve_forever()
