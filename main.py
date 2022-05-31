#imports
import os
import json
from twilio.rest import Client
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

#variables
account_sid = os.environ['account_sid']
auth_token = os.environ['auth_token']
to_number = os.environ['to_number'] #input your personal phone number as variable
from_number = os.environ['from_number'] #input your twilio number as variable

client = Client(account_sid, auth_token)

#get crypto prices (Bitcoin and Ethereum)

crypto_prices = cg.get_price(ids = 'bitcoin,ethereum', vs_currencies = 'usd')
print (crypto_prices)
crypto_prices_text = json.dumps(crypto_prices)
print (crypto_prices_text)

client.api.account.messages.create(
to = to_number, 
from_ = from_number,
body=crypto_prices_text) #input text message
