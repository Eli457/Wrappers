from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


class CoinMarketCap:

    def __init__(self, key):

        self.url = "https://pro-api.coinmarketcap.com"
        self.parameters = {
            'start': '1',
            'limit': '5000',
            'convert': 'USD'
        }
        self.headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': key
        }
        self.session = Session()
        self.session.headers.update(self.headers)

    def _call_api(self, cate, path, ver='v1'):
        """Returns the json object of the api call """
        try:
            call = "{}/{}/{}/{}?".format(self.url, ver, cate, path)
            response = self.session.get(call, params=self.parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return

    def list_of_currency(self):
        """Returns the names of all of the cryptocurrencies from
            oldest to newest and their values
        """

        call = self._call_api('cryptocurrency', 'listings/latest')

        names = []

        for name in call['data']:
            names.append(name['name'])

        exchange = []

        data = call['data']
        for d in data:
            quote = d['quote']
            usd = quote['USD']
            exchange.append(usd['price'])

        return names, exchange

    def print(self):
        """Prints the names and corresponding values of the cryptocurrencies"""

        names, values = self.list_of_currency()

        for n, v in zip(names, values):
            print('The cryptocurrency {} is currently valued at {} USD.'.format(n, v))

    def graph_on(self):
        """Creates a scatter plot of names and corresponding values of the
            cryptocurrencies from oldest to newest
        """
        x, y = self.list_of_currency()

        plt.scatter(x, y)
        plt.xlabel('Oldest -> Newest')
        plt.ylabel('Current value(USD)')
        plt.xticks(rotation=90)

        plt.show()
        pass

    def graph_tt(self, graph=True):
        """Creates a graph of the top ten cryptocurrencies(optional) and returns
        a list of top ten"""

        names, values = self.list_of_currency()

        comb = []

        for n, v in zip(names, values):
            comb.append([n, v])

        comb.sort(key=lambda z: z[1])
        comb.reverse()

        top = []
        for item in range(10):
            top.append(comb[item])

        if graph:

            x = []
            y = []

            for item in top:
                x.append(item[0])
                y.append(item[1])

            plt.plot(x, y)
            plt.xlabel('Top 10')
            plt.ylabel('Current value(USD)')
            plt.xticks(rotation=90)

            plt.show()

        return top

    def get_metadata(self):

        call = self._call_api('cryptocurrency', 'info')

        pass







