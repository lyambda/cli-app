import requests

token = ''
auth = False
email = ''
link = 'https://lyabmda12345.herokuapp.com/'

def request(method, t_bool, args):
    global token
    res = ''
    if t_bool:
        res = requests.get(f'{link}/{method}?token={t_bool}&{args}')
    else:
        res = requests.get(f'{link}/{method}?{args}')
    if res.status_code == 200:
        return res.json()
    else:
        print(res.status_code)
        print(res.text)

class Auth():
    def sendCode(email):
        res = request('sendCode', False, f'email={email}')
        if res['ok']:
            print('Code send to email...')
        else:
            raise Exception(res['description'])

    def join(code):
        res = request('signIn', False, f'email={email}&code={code}')
        token = res['token']
        if (res['is_auth']):  # login
            pass
        else:       # register
            Auth.register(token)
        return token

    def register(token):
        name = input("Name >>> ")
        surname = input("Surname >>> ")
        description = input("Description >>> ")
        res = request('register', token, f'name={name}&surname={surname}&description={description}&code={code}')

    def logout(token):
        res = request('logOut', token, '')
        raise Exception('You loged out!')

class Group():
    def createGroup(name, link, description):
        #res = request('createGroup', True, f'')
        pass

    def joinGroup(token, id_group):
        #res = request('joinGroup', True, f'')
        pass

    def sendMessage(token, id_group, text):
        #res = request('sendMessage', True, f'')
        pass

    def getMessages(token, id_group):
        #res = request('getMessages', True, f'')
        pass

class Profile():
    def _me():
        res = requests.get(f'{link}/me?session_token={token}').json()
        return res

class InputBox():
    def funcs(text):
        pass

email = input('Email >>> ')
Auth.sendCode(email)
code = input('Code >>> ')
token = Auth.join(code)

# ...

while True:
    text = input("Input: ")
    InputBox.funcs(text)
