Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

======= RESTART: C:/Users/Kira/OneDrive/Desktop/sdev220/M04-16.8/file.py =======
import csv
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        print(book)

        
{'author': 'J R R Tolkien', 'book': 'The Hobbit'}
{'author': 'Lynne Truss', 'book': 'Eats, Shoots & Leaves'}

======= RESTART: C:/Users/Kira/OneDrive/Desktop/sdev220/M04-16.8/file.py =======
import csv
import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
curs.execute('''create table book (title text, author text, year int)''')
<sqlite3.Cursor object at 0x000001EDF5BB3E40>
db.commit()

import csv
import sqlite3
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (book['title'], book['author'], book['year']))

        
Traceback (most recent call last):
  File "<pyshell#20>", line 4, in <module>
    curs.execute(ins_str, (book['title'], book['author'], book['year']))
KeyError: 'title'

======= RESTART: C:/Users/Kira/OneDrive/Desktop/sdev220/M04-16.8/file.py =======
Traceback (most recent call last):
  File "C:/Users/Kira/OneDrive/Desktop/sdev220/M04-16.8/file.py", line 19, in <module>
    for row in db.execute(sql):
NameError: name 'db' is not defined

======= RESTART: C:/Users/Kira/OneDrive/Desktop/sdev220/M04-16.8/file.py =======
import csv
import sqlite3
ins_str = 'insert into book values(?, ?, ?)'
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (f'{'title'}, book{'author'}, book{'year'}))
                               
SyntaxError: unterminated string literal (detected at line 4)
with open('books.csv', 'rt') as infile:
    books = csv.DictReader(infile)
    for book in books:
        curs.execute(ins_str, (f'{'title'}, book{'author'}, book{'year'}))
                               
SyntaxError: unterminated string literal (detected at line 4)
