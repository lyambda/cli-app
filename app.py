import requests, json

link = 'https://lyabmda.herokuapp.com/'

def config():
    with open('config.json') as jsonfile:
        config1 = json.load(jsonfile)
    token = config1["token"]
    print(token)
    return token

def request(method, t_bool, args):
    res = ''
    if t_bool:
        a = {'token': config()}
        if args != '':
            res = requests.post(f'{link}/{method}', data={**a, **args})
        else:
            res = requests.post(f'{link}/{method}', data=a)
    else:
        res = requests.post(f'{link}/{method}', data=args)
    print(res.status_code)
    print(res.text)

    if res.status_code == 200:
        return res.json()

class Auth():
    def sendCode(email):
        res = request('sendCode', False, {'email': email})
        if res['ok']:
            print('Code send to email...')
        else:
            raise Exception(res['description'])

    def join(code):
        res = request('signIn', False, {'email': email, 'code': code})
        tokene = res['token']
        f = open(f'config.json', "w")
        f.write('''{"token": "''' + tokene + '''"}''')
        if (res['is_auth']):  # login
            pass
        else:       # register
            Auth.register()
        return tokene

    def register():
        print('You need register:')
        name = input(" Name >>> ")
        surname = input(" Surname >>> ")
        description = input(" Description >>> ")
        res = request('register', True, 
            {
                'name': name, 
                'surname': surname, 
                'description': description, 
                'code': code
            }
        )

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
        res = request('createGroup', True, 
            {
                'name': name, 
                'link': link, 
                'description': description
            }
        )
        return res

    def joinGroup():
        id_group = input(" Group ID >>> ")
        res = request('joinGroup', True, {'id_group': id_group})
        return res

    def sendMessage():
        id_group = input(" Group ID >>> ")
        text = input(" Text >>> ")
        res = request('sendMessage', True, {'id_group': id_group, 'text': text})
        return res

    def getMessages():
        id_group = input(" Group ID >>> ")
        res = request('getMessages', True, {'id_group': id_group})
        return res

class Profile():
    def _me():
        res = res = request('me', True, '')
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

def box():
    while True:
        text = input("Input command: ")
        InputBox.funcs(text)

if config():
    box()
else:
    print('You need auth:')
    email = input(' Email >>> ')
    Auth.sendCode(email)
    code = input(' Code >>> ')
    Auth.join(code)
    box()
