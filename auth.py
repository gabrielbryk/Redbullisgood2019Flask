from pyramid.response import Response
import json

class Auth:
    def __init__(self, request):
        self.request = request

    def getToken(self):
        data = self.request.body.decode('utf8').replace("'", '"')
        data = json.loads(data)
        token = data['token']
        return token