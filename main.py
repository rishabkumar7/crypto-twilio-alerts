#imports
import os
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

#print (cg.get_price(ids='bitcoin,ethereum', vs_currencies='usd'))
crypto_prices = cg.get_price(ids = 'bitcoin,ethereum', vs_currencies = 'usd')
print (crypto_prices)

client.api.account.messages.create(
to = to_number, 
from_ = from_number,
body="Hey There") #input text message
