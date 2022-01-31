import urllib.request, urllib.parse, urllib.error
import twurl
import json
import sqlite3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

conn = sqlite3.connect('mytwdata.sqllite')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS People
            (id INTEGER PRIMARY KEY, name TEXT
UNIQUE, retrived INTEGER)''')

cur.execute('''CREATE TABLE IF NOT EXISTS Follows
            (from_id INTEGER, to_id INTEGER,
UNIQUE(from_id, to_id))''')

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    acct = input('Enter the acct name, or quit: ')
    if (acct == 'quit') : break
    if (len(acct) < 1 ):
        cur.execute('SELECT id, name FROM People WHERE retrived=0 LIMIT 1')
        try:
            (id, acct) = cur.fetchone()
        except:
            print('no unretrived Twitter accounts found')
            continue
    else:
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (acct, ))
        try:
            id = cur.fetchone()[0]
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrived) VALUES (?, 0)''', (acct, ))
            conn.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', acct)
                continue
            id = cur.lastrowid
    
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '100'})
    print('retriving acct', acct)

    try:
        connection = urllib.request.urlopen(url, context=ctx)
    except Exception as err:
        print('Failed to Retrieve', err)
        break

    data = connection.read().decode()
    headers = dict(connection.getheaders())

    printdata('Remaing', headers['x-rate-limit-remaining'])

    try:
        js = json.loads(data)
    except: 
        print('unable to parse data')
        print(data)
        continue

    if 'users' not in js: 
        print('Incorrect JSON received')
        print(json.dumps(js, indent=4))
        continue

    cur.execute('UPDATE PEOPLE SET retrieved = 1 WHERE name = ?', (acct, ))

    countnew = 0
    countold = 0
    for u in js:
        friend = u['screen_name']
        print(friend)
        cur.execute('SELECT id FROM People WHERE name = ? LIMIT 1',
                    (friend, ))
        try:
            friend_id = cur.fetchone()[0]
            countold = countold + 1
        except:
            cur.execute('''INSERT OR IGNORE INTO People (name, retrived)
                        VALUES (?, 0)''', (friend, ))
            con.commit()
            if cur.rowcount != 1:
                print('Error inserting account:', friend)
                continue
            friend_id = cur.lastrowid
            countnew = countnew + 1
        cur.execute('''INSERT OR IGNORE INTO FOLLOW (from_id, to_id)
                    VALUES (?, ?)''', (id, friend_id))
    print('New accounts=', countnew, 'revisited=', countold)
    print('remaining', headers['x-rate-limit-remaining'])
    conn.commit()
cur.close()