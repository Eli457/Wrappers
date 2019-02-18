from settings import *
import urllib3
import json
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class CmcApi:

    def __init__(self):

        self.url = URL + 'CMC_PRO_API_KEY=' + API_KEY
        self.api_key = API_KEY
        self.call = None

    def call_api(self):
        """Returns the json object of the api call """
        return json.loads(urllib3.PoolManager().request('GET', self.url).data.decode('UTF-8'))

    def list_of_currency(self):
        """Returns the names of all of the cryptocurrencies from
            oldest to newest
        """
        if self.call is None:
            self.call = self.call_api()

        names = []

        for name in self.call['data']:
            names.append(name['name'])

        return names

    def exchange_usd(self):
        """Returns the current values of all of the cryptocurrencies from
            oldest to newest
        """
        if self.call is None:
            self.call = self.call_api()

        exchange = []

        data = self.call['data']
        for d in data:
            quote = d['quote']
            usd = quote['USD']
            exchange.append(usd['price'])

        return exchange

    def print(self):
        """Prints the names and corresponding values of the cryptocurrencies"""

        names = self.list_of_currency()

        values = self.exchange_usd()

        for n, r in zip(names, values):
            print('The cryptocurrency {} is currently valued at {} USD.'.format(n, r))

    def graph(self):
        """Creates a scatter plot of names and corresponding values of the
            cryptocurrencies
        """
        names = self.list_of_currency()

        values = self.exchange_usd()

        plt.scatter(names, values)
        plt.xlabel('Oldest -> Newest')
        plt.ylabel('Current value(USD)')
        plt.xticks(rotation=90)

        plt.show()
        








