import flask
from flask import request
from flask_cors import CORS
from service import Service

server = flask.Flask(__name__)

CORS(server)
@server.route('/status',methods=['GET'])
def getStatus():
    status = Service.getStatus()
    obj={"status":status}
    return obj

if __name__ == '__main__':
    server.run()
