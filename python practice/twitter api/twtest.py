import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print('* calling twitter...')
url = augment('https://api.twitter.com/1.1/statuses/user_timeline.json',
                {'screen_name': 'drchuck', 'count': '2'})

print(url)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

connnection = urllib.request.open(url, context)
data = connnection.read()
print(data)

headers = dict(connnection.getheaders())
print(headers)