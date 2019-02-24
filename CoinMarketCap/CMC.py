import requests
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


class CoinMarketCap:

    def __init__(self, key):

        self.url = "https://pro-api.coinmarketcap.com"
        self.api_key = key

    def _call_api(self, cate, path, ver='v1'):
        """Returns the json object of the api call """
        call = self.url + '/' + ver + '/' + cate + '/' + path + '?' + 'CMC_PRO_API_KEY=' + self.api_key
        r = requests.get(call)
        return r.json()

    def list_of_currency(self):
        """Returns the names of all of the cryptocurrencies from
            oldest to newest
        """

        call = self._call_api('cryptocurrency', 'listings/latest')

        names = []

        for name in call['data']:
            names.append(name['name'])

        return names

    def exchange_usd(self):
        """Returns the current values of all of the cryptocurrencies from
            oldest to newest
        """
        call = self._call_api('cryptocurrency', 'listings/latest')

        exchange = []

        data = call['data']
        for d in data:
            quote = d['quote']
            usd = quote['USD']
            exchange.append(usd['price'])

        return exchange

    def print(self):
        """Prints the names and corresponding values of the cryptocurrencies"""

        names = self.list_of_currency()

        values = self.exchange_usd()

        for n, v in zip(names, values):
            print('The cryptocurrency {} is currently valued at {} USD.'.format(n, v))

    def graph_on(self):
        """Creates a scatter plot of names and corresponding values of the
            cryptocurrencies from oldest to newest
        """
        x = self.list_of_currency()

        y = self.exchange_usd()

        plt.scatter(x, y)
        plt.xlabel('Oldest -> Newest')
        plt.ylabel('Current value(USD)')
        plt.xticks(rotation=90)

        plt.show()

    def graph_tt(self, graph=True):
        """Creates a graph of the top ten cryptocurrencies(optional) and returns
        a list of top ten"""

        names = self.list_of_currency()

        values = self.exchange_usd()

        comb = []

        for n, v in zip(names, values):
            comb.append([n, v])

        comb.sort(key=lambda x: x[1])
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







