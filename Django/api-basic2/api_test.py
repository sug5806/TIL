import requests

def get_token(username, password):
    data = {
        'username': username,
        'password': password,

    }

    req = requests.post('http://127.0.0.1:8000/api/get_token/', data=data)
    data = req.json()
    if 'token' in data:
        return data['token']
    else:
        None


def get_userlist():
    token = get_token('sug5806', 'ghd9413')
    if token:
        headers = {
            'Authorization': 'Token ' + token
        }

        req = requests.post('http://127.0.0.1:8000/api/accounts/', headers=headers.items)
        data = req.json()
        if data:
            return data
        else:
            return None

    else:
        raise ValueError('Token Error ')
