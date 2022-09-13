from crypt import methods
from sys import getallocatedblocks
from flask import Flask, request
import json
from generic_json_encoder import GenericEncoder
from person_repository import GetAll, GetByKey
app = Flask(__name__)

def CheckInputs(inputs, requires):
    for param in requires:
            if param not in inputs:
                return (json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'

@app.route('/users', methods = ['GET'])
def get_users():
    return json.dumps(GetAll(), cls=GenericEncoder)

@app.route('/user/<userName>')
def get_user_by_name(userName):
    return json.dumps(GetByKey(userName))

if __name__ == '__main__':
    app.run(debug = True)