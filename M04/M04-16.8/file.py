text = '''author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''
with open('test.csv', 'wt') as outfile:
    outfile.write(text)

text = '''title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Miéville,2000
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books2.csv', 'wt') as outfile:
    outfile.write(text)

import csv
import sqlite3
db = sqlite3.connect('books.db')
curs = db.cursor()
sql = 'select title from book order by title asc'
for row in db.execute(sql):
    print(row)
