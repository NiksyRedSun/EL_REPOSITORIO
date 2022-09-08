from flask import Flask, request
import json
import random
from person import Person
from json_file_worker import loading, saving
from more_functions import functions_keys, functions_dict

app = Flask(__name__)

names = ['john', 'jack', 'bill', 'sady', 'chavier', 'charles', 'arthur', 'leopold', 'shon', 'caren']

def CheckInputs(inputs, requires):
    for param in requires:
            if param not in inputs:
                return (json.dumps({'status': 'data_error', 'message': f'{param} expected'}), 400)
    return 'passed'

@app.route('/functions')
def functions_page():
    return functions_keys

@app.route('/<function>')
def function_page(function):
    return functions_dict[function]

@app.route('/')
def start_page():
    return 'You are welcome at SLOVNIK, check /functions for more functions'

@app.route('/users')
def show_users_profile():
    slovnik = loading()
    slovnik_info = ''
    for value in slovnik.values():
        slovnik_info += str(value.short_info()) + '; '
    return slovnik_info

@app.route('/user/<user>')
def show_user_profile(user):
    slovnik = loading()
    if user in slovnik:
        return slovnik[user].info()
    else:
        return 'You are looking for the wrong person'

@app.route('/user/<user>', methods=['DELETE'])
def delete_user_profile(user):
    slovnik = loading()
    if user in slovnik:
        del slovnik[user]
        deleted_data = user.capitalize() + ' ' + 'had deleted even before you thought about it'
        saving(slovnik)
        return deleted_data
    else:
        return 'You are trying to delete unregistered person'


@app.route('/user/<user>', methods=['POST'])
def post_user_profile(user):
    inputs = request.get_json()
    check = CheckInputs(inputs,  ['name', 'age'])
    slovnik = loading()
    if check != 'passed':
        return check
    if user not in slovnik:
        age = inputs['age']
        user = Person(user, age)
        slovnik[user.name] = user
        posted_data = (user.name).capitalize() + ' ' + 'has been successfully added to dictionary'
        saving(slovnik)
        return posted_data
    else:
        return 'This person is alredy on the list'

@app.route('/postrandom', methods=['POST'])
def post_random_profile():
    slovnik = loading()
    if len(names) > 0:
        name = random.choice(names)
        age = random.randint(16, 55)
        user = Person(name, age)
        names.remove(name)
        slovnik[user.name] = user
        saving(slovnik)
        posted_data = (user.name).capitalize() + ' ' + 'that is ' + str(user.age) + ' ' + 'has been successfully added to dictionary'
        return posted_data
    else:
        return 'There is no free nicknames left'

@app.route('/user/<user>', methods=['PUT'])
def put_user_profile(user):
    slovnik = loading()
    inputs = request.get_json()
    check = CheckInputs(inputs, ['name', 'age'])
    if check != 'passed':
        return check
    if user in slovnik:
        prevname = user.capitalize()
        name = inputs['name']
        age = inputs['age']
        del slovnik[user]
        user = Person(name, age)
        slovnik[user.name] = user
        posted_data = prevname + ' has been changed successfully for ' + (user.name).capitalize()
        saving(slovnik)
        return posted_data
    else:
        return 'You are trying to change unregistered person'

if __name__ == '__main__':
    app.run(debug = True)