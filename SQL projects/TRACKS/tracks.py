import xml.etree.ElementTree as ET
import sqlite3

conn = sqlite3.connect('tracks.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id   INTEGER,
    title    TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title    TEXT UNIQUE,
    album_id    INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);

''')

fname = input('open the file: ')
if len(fname) < 1 : fname = 'Library.xml'

# <key>Track ID</key><integer>369</integer>
# <key>Name</key><string>Another One Bites The Dust</string>
# <key>Artist</key><string>Queen</string>

def lookup(d, key):
    found = False
    for child in d:
        if found : return child.text
        if child.tag == "key" and child.text == key :
            found = True
    return None

sutff = ET.parse(fname)
all = sutff.findall('dict/dict/dict')
print('Dict Count: ', len(all))

for entry in all:
    if (lookup(entry, 'Track ID') is None ) : continue
    
    name = lookup(entry, 'Name')
    artist = lookup(entry, 'Artist')
    album = lookup(entry, 'Album')
    count = lookup(entry, 'Play Count')
    rating = lookup(entry, 'Rating')
    length = lookup(entry, 'Total Time')
