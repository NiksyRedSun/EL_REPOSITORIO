from flask import Flask, request
import json
from person import person_repository, Person

app = Flask(__name__)


def CheckInputs(inputs, requires):
    for param in requires:
            if param not in inputs:
                return (json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'


@app.route('/')
def start_page():
    return 'You are welcome at SLOVNIK'


@app.route('/users')
def get_users_profile():
    return person_repository().show()


@app.route('/user/<id>')
def get_user_profile(id):
    return person_repository().show(Person(id=id))


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_profile(id):
    return person_repository().delete(Person(id=id))


@app.route('/user', methods=['POST'])
def post_user_profile():
    inputs = request.get_json()
    check = CheckInputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return person_repository().create(Person(name=name, age=age))


@app.route('/user/<id>', methods=['PUT'])
def put_user_profile(id):
    inputs = request.get_json()
    check = CheckInputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return person_repository().update(Person(id=id, name=name, age=age))


if __name__ == '__main__':
    app.run(debug = True)