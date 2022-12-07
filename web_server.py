from flask import Flask, request
import json
from person_repository import person_repository
from person import Person

app = Flask(__name__)

__person_repository = person_repository()


def __сheck_inputs(inputs, requires):
    for param in requires:
            if param not in inputs:
                raise Exception(json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'


@app.route('/')
def start_page():
    return 'You are welcome at training_project "first_ws"'


@app.route('/users')
def get_users_profile():
    return __person_repository.get()


@app.route('/user/<id>')
def get_user_profile(id):
    return __person_repository.get(Person(id=id))


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_profile(id):
    return __person_repository.delete(Person(id=id))


@app.route('/user', methods=['POST'])
def post_user_profile():
    inputs = request.get_json()
    check = __сheck_inputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return __person_repository.create(Person(name=name, age=age))


@app.route('/user/<id>', methods=['PUT'])
def put_user_profile(id):
    inputs = request.get_json()
    check = __сheck_inputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return __person_repository.update(Person(id, name, age))


if __name__ == '__main__':
    app.run(debug = True)