import logging
import requests
import pprint

logger = logging.getLogger()

# "https://fapi.binance.com"
# "https://testnet.binancefuture.com"

# "wss://fstream.binance.com"

def get_contracts():

    response_object = requests.get("https://testnet.binancefuture.com/fapi/v1/exchangeInfo")
    print(response_object.status_code)
    pprint.pprint(response_object.json())

    contracts = []

    for contract in response_object.json()['symbol']:
        contracts.append(contract['pair'])

get_contracts()