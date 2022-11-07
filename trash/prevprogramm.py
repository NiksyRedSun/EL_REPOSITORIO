from flask import Flask, request
import json
app = Flask(__name__)

slovnik = {
    'Niksy':{'name':'Niksy', 'age':25},
    'Max':{'name':'Max', 'age':23},
    'Joe':{'name':'Joe', 'age':45},
    'Antonio':{'name':'Antonio', 'age':49}
}

names = ['John', 'Jack', 'Bill', 'Sady', 'Chavier', 'Charles', 'Arthur', 'Leopold', 'Shon', 'Caren']
nicknames = ['Bear', 'Wolf', 'BadBoy', 'Chainsaw', 'Rabbit', 'Gun', 'Eagle', 'Bull']

@app.route('/users')
def index():
    return json.dumps(slovnik)

@app.route('/user/<username>')
def show_user_profile(username):
    if username in slovnik:
        return json.dumps(slovnik[username])
    else:
        return json.dumps('You are looking for the wrong person')

@app.route('/user/<username>', methods=['DELETE'])
def delete_user_profile(username):
    if username in slovnik:
        del slovnik[username]
        deleted_data = str(username) + ' ' + 'had deleted even before you thought about it'
        return json.dumps(deleted_data)
    else:
        return json.dumps('You are trying to delete unregistered person')

@app.route('/user/<username>', methods=['POST'])
def post_user_profile(username):
    if username not in slovnik:
        inputs = request.get_json()
        name = inputs['name']
        age = inputs['age']
        slovnik[username] = {'name':name, 'age':age}
        posted_data = str(username) + ' ' + 'has been successfully added to dictionary'
        return json.dumps(posted_data)
    else:
        return json.dumps('This person is alredy on the list')

@app.route('/postrandom', methods=['POST'])
def post_random_profile():
    if len(nicknames) > 0:
        name = random.choice(names)
        age = random.randint(16, 55)
        username = random.choice(nicknames)
        nicknames.remove(username)
        slovnik[username] = {'name':name, 'age':age}
        posted_data = str(username) + ' ' + 'that is called' + ' ' + str(name) + ' ' + 'and his age is'+ ' ' + str(age) \
                      + ' ' + 'has been successfully added to dictionary'
        return json.dumps(posted_data)
    else:
        return json.dumps('There is no free nicknames left')

@app.route('/user/<username>', methods=['PUT'])
def put_user_profile(username):
    if username in slovnik:
        inputs = request.get_json()
        name = inputs['name']
        age = inputs['age']
        slovnik[username] = {'name':name, 'age':age}
        posted_data = str(username) + ' ' + 'has been changed successfully'
        return json.dumps(posted_data)
    else:
        return json.dumps('You are trying to change unregistered person')

if __name__ == '__main__':
    app.run(debug = True, port = 5001)