import requests
from pprint import pprint

def requests_exchange_rates(currencies,source):

    api_key = '61b46f0c3ab3a123c4929bba8833d881'

    dates_requests = requests.get(f'http://apilayer.net/api/live?access_key={api_key}&source={currencies}&currencies={source}')
    list_currency = dates_requests.json()

    output_value = round(list_currency['quotes'][f'{currencies + source}'], 3)

    return output_value