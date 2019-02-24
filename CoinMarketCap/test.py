from CMC import CoinMarketCap
from settings import *

call = CoinMarketCap(API_KEY)

#names = call.list_of_currency()

#values = call.exchange_usd()

#call.print()

#call.graph_on()

tt = call.graph_tt()

print(tt)
