import requests

token = ''
auth = False
link = 'https://lyambda123244.herokuapp.com'

class Auth():
    def sendCode(email):
        res = requests.get(f'{link}/sendCode?email={email}').json()
        if res['ok']:
            token = res['session_token']
            auth = res['is_authenticated']
        else:
            raise Exception(res['description'])

    def join(code):
        res = ''
        if (auth):  # login
            res = requests.get(f'{link}/login?session_token={token}&code={code}').json()
        else:       # register
            res = requests.get(f'{link}/register?session_token={token}&code={code}').json()

    def logout():
        res = requests.get(f'{link}/logOut?session_token={token}').json()
        raise Exception('You loged out!')

class Group():
    def createGroup(name, link, description):
        pass

    def joinGroup(id_group):
        pass

    def sendMessage(id_group, text):
        pass

    def getMessages(id_group):
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
