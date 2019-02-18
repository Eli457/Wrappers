import CMC

call = CMC.CmcApi()

names = call.list_of_currency()

values = call.exchange_usd()

call.print()

call.graph()




