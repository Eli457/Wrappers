from settings import *
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class CmcApi:

    def __init__(self):
        self.url = URL + 'CMC_PRO_API_KEY=' + API_KEY
        self.api_key = API_KEY
        self.call = None

    def call_api(self):
        request = urllib3.PoolManager().request('GET', self.url)
        return json.loads(request.data.decode('UTF-8'))

    def list_of_currency(self):
        if self.call is None:
            self.call = self.call_api()

        names = []

        for name in self.call['data']:
            names.append(name['name'])

        return names

    def exchange_usd(self):
        if self.call is None:
            self.call = self.call_api()

        exchange = []

        data = self.call['data']
        for d in data:
            quote = d['quote']
            usd = quote['USD']
            exchange.append(usd['price'])

        return exchange







