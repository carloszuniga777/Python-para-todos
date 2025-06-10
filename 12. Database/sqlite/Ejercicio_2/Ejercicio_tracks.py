import sqlite3
import os

# Obtener la ruta del directorio actual del script
script_dir = os.path.dirname(os.path.abspath(__file__))
    
# Construir la ruta completa para la base de datos
db_path = os.path.join(script_dir, 'trackdb.sqlite')

conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Track;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Artist;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY 
        AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')


#--------- Contruir la ruta del archivo--------------- 

# Construye la ruta al archivo independientemente de dónde se abra el proyecto
file_path = os.path.join(script_dir, "..", "tracks", 'tracks.csv')                       ## Subir solo 1 niveles (..)
file_path = os.path.abspath(file_path)

#------------------------------------------------------

#Abre el archivo tracks.cvs
handle = open(file_path, 'r')


# Another One Bites The Dust,Queen,Greatest Hits,55,100,217103
#   0                          1      2           3  4   5

for line in handle:
    line = line.strip()
    pieces = line.split(',')
    if len(pieces) < 6 : continue

    name = pieces[0]
    artist = pieces[1]
    album = pieces[2]
    count = pieces[3]
    rating = pieces[4]
    length = pieces[5]
    genero = pieces[6]

    print(name, artist, album, count, rating, length)

    cur.execute('''INSERT OR IGNORE INTO Artist (name) 
        VALUES ( ? )''', ( artist, ) )
    
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) 
        VALUES ( ?, ? )''', ( album, artist_id ) )
    
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
    album_id = cur.fetchone()[0]


    cur.execute('''INSERT OR IGNORE INTO Genre(name) 
                   VALUES( ?)''', (genero,))
    
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genero, ))
    genero_id = cur.fetchone()[0]
    

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', 
        ( name, album_id, genero_id, length, rating, count ) )

    conn.commit()
