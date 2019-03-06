from CMC import CoinMarketCap
from settings import *

call = CoinMarketCap(API_KEY)

call.print()

# call.graph_on()

tt = call.graph_tt()

print(tt)
