import sqlite3
from datetime import *

date = date.today()


class Luggage:
    def __init__(self, name='', hmany='', luggagetxt=''):
        self.name = name
        self.hmany = hmany
        self.luggagetxt = luggagetxt

    def inputluggage(self):
        self.name = input("Podaj imię i nazwisko: ")
        self.hmany = int(input("Ile bagaży? "))
        self.luggagetxt = ['Imię i nazwisko: %s\nIlość bagaży: %s\nKiedy zostawiono: %s\n' % (self.name,
                                                                                              str(self.hmany),
                                                                                              str(date))]

    def txtsaving(self):
        with open('bagaze.txt', 'a') as f:
            for linia in self.luggagetxt:
                f.write(linia + '\n')  # saving to bagaze.txt

    def dbsaving(self):
        con = sqlite3.connect('hotel.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS luggage (
                intdate varchar(250) DEFAULT '',
                cname varchar(250) DEFAULT '',
                hmany varchar(250) DEFAULT ''
            )""")

        cur.execute("""
        INSERT OR IGNORE INTO luggage (intdate, cname, hmany)
        VALUES (?,?,?)
        """, (date, self.name, self.hmany))
        con.commit()
