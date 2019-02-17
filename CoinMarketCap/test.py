import CMC

names = CMC.CmcApi().list_of_currency()

values = CMC.CmcApi().exchange_usd()

for n, r in zip(names, values):
    print('The cryptocurrency {} is currently valued at {} USD.'.format(n, r))


