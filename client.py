import sqlite3
from datetime import *

date = date.today()


class Client:
    def __init__(self, name='', passport='', birth='', company=''):
        self.name = name
        self.passport = passport
        self.birth = birth
        self.company = company

    def inputuserdata(self):
        self.name = input("Podaj imię i nazwisko: ")
        self.passport = input("Podaj numer paszportu: ")
        self.birth = input("Podaj datę urodzenia: ")
        self.company = input("Jaka firma? ")

    def clientdb(self):
        con = sqlite3.connect('klienci.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                passport varchar(250) DEFAULT '',
                cname varchar(250) DEFAULT '',
                birth varchar(250) DEFAULT '',
                company varchar(250) DEFAULT '',
                intdate varchar(250) DEFAULT ''
                )""")

        cur.execute("""
        INSERT OR REPLACE INTO clients (passport, cname, birth, company, intdate)
        VALUES (?,?,?,?,?)
        """, (self.passport, self.name, self.birth, self.company, date))
        con.commit()
