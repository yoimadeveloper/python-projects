import sqlite3

conn = sqlite3.connect('mydata.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Mohit')

cur.execute('''
CREATE TABLE Mohit (email TEXT, count INTEGER)''')

fname = input('open the file: ')
if (len(fname) < 1) : fname = 'mbox-short.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: ') : continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Mohit WHERE email = ?', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Mohit (email, count) VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Mohit SET count = count + 1 WHERE email = ?', (email,))
    
    conn.commit()

sqlstr = 'SELECT email, count FROM Mohit ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str,(row[0]), row[1])

cur.close()