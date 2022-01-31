import urllib.request, urllib.parse, urllib.error
import twurl
import ssl
import json


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acc = input('input the account: ')
    if (len(acc) < 1) : break
    url = twurl.augment(TWITTER_URL,  
                        {'screen_name': acc, 'count': 5})
    print('retriving', url)
    connnection = urllib.request.urlopen(url, context=ctx)
    data = connnection.read().decode()
    headers = dict(connnection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)
    print(json.dumps(js, indent=4))
    
    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print(' ', s[:50])