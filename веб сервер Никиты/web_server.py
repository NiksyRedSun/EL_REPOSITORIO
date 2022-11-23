from flask import Flask, request
import json
from person import persons, person

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
def show_users_profile():
    return persons().show_all_persons()


@app.route('/user/<id>')
def show_user_profile(id):
    return person(id).show_one_person()


@app.route('/user/<id>', methods=['DELETE'])
def delete_user_profile(id):
    return person(id).delete_one_person()


@app.route('/user/post', methods=['POST'])
def post_user_profile():
    inputs = request.get_json()
    check = CheckInputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return persons().post_one_person(name, age)


@app.route('/user/<id>', methods=['PUT'])
def put_user_profile(id):
    inputs = request.get_json()
    check = CheckInputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    name = inputs['name']
    age = inputs['age']
    return person(id).change_person_profile(name, age)


if __name__ == '__main__':
    app.run(debug = True)