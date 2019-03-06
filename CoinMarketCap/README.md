#CoinMarketCap

CoinMarketCap is a RESTful Python Library that wraps the Coin Market Cap(a cryptocurrency data website) API.

#Usage

```python
from CMC import CoinMarketCap

CoinMarketCap('api_key').list_of_currency() #returns list of cryptocurrencies names and values

CoinMarketCap('api_key').print() #prints currency name and value

CoinMarketCap('api_key').graph_tt()#graphs and returns top ten currency values

CoinMarketCap('api_key').get_metadata()#returns metadata

```