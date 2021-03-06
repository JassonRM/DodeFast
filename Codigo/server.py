from flask import Flask
from flask_restful import Api, Resource, reqparse
import json
from threading import Thread
from flask_socketio import SocketIO, emit


class Server():
    def __init__(self, ide):
        serverThread = Thread(target=self.run, args=(ide,))
        serverThread.daemon = True
        serverThread.start()

    def run(self, ide):
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(Code, "/code", resource_class_kwargs={'ide': ide})
        socket = SocketIO(app)
        socket.run(app, host='0.0.0.0')

class Code(Resource):
    def __init__(self, **kwargs):
        self.ide = kwargs['ide']

    def get(self):
        return json.dumps(self.ide.getCode())

