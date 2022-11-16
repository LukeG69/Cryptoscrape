from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import keysbruh
from twilio.rest import Client
from re import sub
from decimal import Decimal



##############FOR MACS THAT HAVE ERRORS LOOK HERE################
## https://timonweb.com/tutorials/fixing-certificate_verify_failed-error-when-trying-requests_html-out-on-mac/

############## ALTERNATIVELY IF PASSWORD IS AN ISSUE FOR MAC USERS ########################
##  > cd "/Applications/Python 3.6/"
##  > sudo "./Install Certificates.command"


#url = 'https://www.tradingview.com/markets/stocks-usa/market-movers-gainers/'
url = 'https://www.livecoinwatch.com/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
TwilioNumber = "+12057089915"
myCellNumber = "+12145642260"
		
req = Request(url, headers=headers)

webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, 'html.parser')


title = soup.title

#print(title.text)


tablecells = soup.findAll('td')

counter = 0

for x in range(5):
    rank = tablecells[counter].text
    name = tablecells[counter+1].text
    price = tablecells[counter+2].text
    change = tablecells[counter+7].text
    


    print(f"Coin Rank: {rank}")
    print(f"Coin Name: {name}")
    print(f"Coin Price: {price}")
    print(f"% Change: {change}")
    print()
    print()


    if str(name) == "BTC Bitcoin":
        value1 = price.replace('$', '')
        value = value1.replace(',', '')
        if value < 40000:
            textmsg = Client.messages.create(to = myCellNumber, from_ = TwilioNumber, body = "Bitcoin is below $40,000")

    if str(name) == "ETH Ethereum":
        value1 = price.str.replace('$', '')
        value = value1.str.replace(',', '')
        if value < 3000:
            textmsg = Client.messages.create(to = myCellNumber, from_ = TwilioNumber, body = "Ethereum is below $3,000")

    counter += 10