from typing import List, Any
from flask import Flask, request, Response
import json
from generic_json_encoder import GenericEncoder
from person_repository import get_by_key, get_all, delete_by_key, \
    add_user, update_user
from validation_error import ValidationError
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    # Это HTML - на затравочку
    return "<p>Стартовая страница.</p>"


@app.route('/users', methods=['GET'])
def get_users():
    return Response(json.dumps(get_all(), cls=GenericEncoder), status=200,
                    mimetype='application/json')


@app.route('/user/<userName>', methods=['GET'])
def get_user_by_name(userName):
    person = get_by_key(userName)
    if (person is None):
        raise KeyError('Not found such Person')
    return Response(json.dumps(person, cls=GenericEncoder),
                    status=200,
                    mimetype='application/json')


@app.route('/user/<userName>', methods=['POST'])
def create_user_by_name(userName):
    inputs = request.get_json()
    _check_inputs(inputs,  ['name', 'age'])
    _guard_equal(userName, inputs['name'])
    add_user(userName, inputs['age'])
    return Response('Added',
                    status=201,
                    mimetype='application/json')


@app.route('/user/<userName>', methods=['PUT'])
def update_user_by_name(userName):
    inputs = request.get_json()
    _check_inputs(inputs,  ['name', 'age'])
    _guard_equal(userName, inputs['name'])
    update_user(userName, inputs['age'])
    return Response('Updated',
                    status=200,
                    mimetype='application/json')


@app.route('/user/<userName>', methods=['DELETE'])
def delete_user_by_name(userName):
    delete_by_key(userName)
    return Response('Deleted or skipped (if not exist)',
                    status=200,
                    mimetype='application/json')


def _check_inputs(inputs: Any, requires: List[str]) -> None or Exception:
    for param in requires:
        if param not in inputs:
            raise ValidationError(f'{param} is not filled')


def _guard_equal(first: Any, second: Any) -> None or Exception:
    if (first != second):
        raise ValidationError(f'{first} and {second} are not equal')


if __name__ == '__main__':
    app.run(debug=True)
