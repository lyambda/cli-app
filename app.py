import requests, json

link = 'https://lyabmda12345.herokuapp.com/'

def config():
    f = open(f'config.json', "r")
    settings = json.loads(f.read())
    token = settings["token"]
    return token

def request(method, t_bool, args):
    token = config()
    res = ''
    if t_bool:
        res = requests.get(f'{link}/{method}?token={token}&{args}')
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
        f = open(f'config.json', "w")
        f.write('''{"token": "''' + token + '''"}''')
        if (res['is_auth']):  # login
            pass
        else:       # register
            Auth.register(token)
        return token

    def register():
        print('You need register:')
        name = input(" Name >>> ")
        surname = input(" Surname >>> ")
        description = input(" Description >>> ")
        res = request('register', True, f'name={name}&surname={surname}&description={description}&code={code}')

    def logout():
        res = request('logOut', True, '')
        f = open(f'config.json', "w")
        f.write('''{"token": ""}''')
        raise Exception('You loged out!')

class Group():
    def createGroup():
        name = input(" Name >>> ")
        link = input(" Link >>> ")
        description = input(" Description >>> ")
        res = request('createGroup', True, f'name={name}&link={link}&description={description}')
        return res

    def joinGroup():
        id_group = input(" Group ID >>> ")
        res = request('joinGroup', True, f'id_group={id_group}')
        return res

    def sendMessage():
        id_group = input(" Group ID >>> ")
        text = input(" Text >>> ")
        res = request('sendMessage', True, f'id_group={id_group}&text={text}')
        return res

    def getMessages():
        id_group = input(" Group ID >>> ")
        res = request('getMessages', True, f'id_group={id_group}')
        return res

class Profile():
    def _me():
        res = res = request('me', True, f'')
        return res

class InputBox():
    def funcs(text):
        cmds = {
            'createGroup': {'func': Group.createGroup, 'args': 3},
            'joinGroup': {'func': Group.joinGroup, 'args': 1},
            'sendMessage': {'func': Group.sendMessage, 'args': 2},
            'getMessages': {'func': Group.getMessages, 'args': 1},
            'me': {'func': Profile._me, 'args': 0},
            'logOut': {'func': Auth.logout, 'args': 0}
        }
        try:
            text = text.split()
            if text[0] in cmds:
                cmd = cmds.get(text[0])
                print(cmd['func']())
                
        except Exception as e:
            print(f"Error: {e}")

while True:
    if config():
        while True:
            text = input("Input command: ")
            InputBox.funcs(text)
    else:
        print('You need auth:')
        email = input(' Email >>> ')
        Auth.sendCode(email)
        code = input(' Code >>> ')
        token = Auth.join(code)
