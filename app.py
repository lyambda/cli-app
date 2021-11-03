import requests

token = ''
auth = False
link = 'https://lyambda123244.herokuapp.com'

def request(method, t_bool, args):
    res = ''
    if t_bool:
        res = requests.get(f'{link}/{method}?session_token={token}&{args}').json()
    else:
        res = requests.get(f'{link}/{method}?{args}').json()
    return res

class Auth():
    def sendCode(email):
        res = request('sendCode', False, f'email={email}')
        if res['ok']:
            token = res['session_token']
            auth = res['is_authenticated']
        else:
            raise Exception(res['description'])

    def join(code):
        res = ''
        if (auth):  # login
            res = request('login', True, f'code={code}')
        else:       # register
            res = request('register', True, f'code={code}')

    def logout():
        res = request('logOut', True, '')
        raise Exception('You loged out!')

class Group():
    def createGroup(name, link, description):
        #res = request('createGroup', True, f'')
        pass

    def joinGroup(id_group):
        #res = request('joinGroup', True, f'')
        pass

    def sendMessage(id_group, text):
        #res = request('sendMessage', True, f'')
        pass

    def getMessages(id_group):
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
Auth.join(code)

# ...

while True:
    text = input("Input: ")
    InputBox.funcs(text)
