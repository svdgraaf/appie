import requests


class Api(object):

    _username = ''
    _password = ''
    _cookies = {}
    _logged_in = False
    _shoppinglist = 0
    _list = None

    def __init__(self, username, password, login=True):
        self._username = username
        self._password = password

        self.login(username, password)

    def login(self, username, password):
        url = 'https://www.ah.nl/mijn/inloggen/basis'

        payload = {
            'userName': username,
            'password': password
        }

        response = requests.post(url, data=payload)
        self._cookies = response.cookies

    def add(self, product_id, quantity=1):
        payload = {
            'type':'PRODUCT',
            'item': {
                'id':str(product_id)
            },
            'quantity': int(quantity),
            'originCode': "PSE"
        }

        url = 'http://www.ah.nl/service/rest/shoppinglists/%d/items' % self._shoppinglist
        response = requests.post(url, cookies=self._cookies, json=payload)
        if response.status_code == 200:
            return True
        else:
            return False

    def _update_list(self):
        url = 'http://www.ah.nl/service/rest/shoppinglists/0/'
        response = requests.get(url, cookies=self._cookies, json=payload)

        self._list = response.json()
        return self._list

    @property
    def list(self):
        return self._list

    def is_on_list(self, product_id):
        if self._list:
            self._update_list()

        counter = 0

        for item in self._list['items']['_embedded']['items']:
            if item['item']['id'] == product_id:
                return item['id']

        # @TODO: return proper exception?
        return None
