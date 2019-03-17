from flask import Flask
from flask_restful import Api, Resource, reqparse
import json

class Server:
    def __init__(self):
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(Code, "/code")
        app.run(host='0.0.0.0', debug=True)




class Code(Resource):
    def get(self):
        list = ["Forward", "Backward", "LOL", "asdf", "asfdasdf", "ahrth", "fdggf", "sgbtd"]
        return json.dumps(list)
