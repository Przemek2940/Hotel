#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

from datetime import date
import datetime
import sqlite3

class Client:
    def __init__(self, name = '', passport = '', birth = '', company = ''):
        self.name = name
        self.passport = passport
        self.birth = birth
        self.company = company

    def inputuserdata(self):
        self.name = input("Podaj imię i nazwisko: ")
        self.passport = input("Podaj numer paszportu: ")
        self.birth = input("Podaj datę urodzenia: ")
        self.company = input("Jaka firma? ")



class Room_management:
    def roomdata(self):  # prints available rooms
        con = sqlite3.connect('pokoje.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM room")
        results = cur.fetchall()
        for row in results:
            print("\nDostępne pokoje:\n%s-osobowy pokój.\nCena: %szł\n" % (row[0], row[1]))


    def roomcreator(self):
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS room (
                beds INTEGER PRIMARY KEY ASC,
                price varchar(250) DEFAULT ''
            )""")

        nbeds = input("Iluosobowy pokój chcesz stworzyć? ")
        nprice = input("Jaka będzie cena za osobę? ")

        cur.execute("""
        INSERT OR IGNORE INTO room (beds, price)
        VALUES (?,?)
        """, (nbeds, nprice))
        con.commit()

    def roomdelete(self):
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f"DELETE from room WHERE beds = '{roomtodelete}'")
        con.commit()
        exit()

    def roomchecking(self):  # searching for room in database
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        if whichroom > 0:
            cur.execute(f"SELECT * from room WHERE beds='{whichroom}'")
            if cur.fetchall():
                return whichroom
            else:
                creatordecision = input(
                    "Nie ma takiego pokoju. Chcesz go stworzyć? (t/n)")  # posibility to create a room
                if creatordecision == 't':
                    r.roomcreator()
                    r.roomdata()
                    r.roomchecking()
                else:
                    print("Błąd1")
        elif whichroom == 0:
            r.roomcreator()
            r.roomdata()
            cur.execute(f"SELECT * from room WHERE beds='{whichroom2}'")
            if cur.fetchall():
                return whichroom2
            else:
                print("Błąd2")

    def amount(self):
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        if whichroom > 0:
            cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom}")
            results = cur.fetchall()
            for row in results:
                return (int(row[0]) * time)
        elif whichroom == 0:  # whichroom2 here too
            cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom2}")
            results = cur.fetchall()
            for row in results:
                return (int(row[0]) * time)


def main(args):                                                        #program screen
    if decision == "1":
        print("%s musi zapłacić %s złotych za meldunek" % (c.name, r.amount()))
    if decision == "2":
        if hmany == 1:
            print("%s zostawił %s bagaż, dnia: %s" % (name, hmany, date))
        elif hmany > 1 and hmany < 5:
            print("%s zostawił %s bagaże, dnia: %s" % (name, hmany, date))
        else:
            print("%s zostawił %s bagaży, dnia %s" % (name, hmany, date))
    elif decision == "3":
        washingcost = hmanywashes * washing
        if hmanywashes == 1:
            print("%s pranie kosztować będzie %szł" % (hmanywashes, washingcost))
        elif hmanywashes > 1 and hmanywashes < 5:
            print("%s prania kosztować będą %szł." % (hmanywashes, washingcost))
        else:
            print("%s prań kosztować będzie %szł." % (hmanywashes, washingcost))
    elif decision == "4":
        print("%s zostawił auto o numerach rejestracyjnych: %s. Dnia: %s" % (name, registrationnumb, date))


decision = input("""Jeśli chcesz kogoś zameldować: wybierz 1.\nJeśli chcesz dodać bagaż: wybierz 2
Jeśli chcesz rozliczyć pralnię: wybierz 3\nJeśli chcesz rozliczyć postój samochodu: wybierz 4
Jeśli chcesz dodać lub usunąć pokój: wybierz 0\n""")
washing = 7
date = date.today()
r = Room_management()
c = Client()

if decision == "1":
    c.inputuserdata()
    r.roomdata()
    whichroom = int(input("Który pokój wybrać? \nJeśli chcesz stworzyć pokój: wybierz 0 \n"))
    if whichroom == 0:
        whichroom2 = int(input("Iluosobowy pokój chcesz wynająć? "))
        r.roomchecking()
    room = input("Numer pokoju: ")
    time = int(input("Ile dni?"))
    checkout = str(date + datetime.timedelta(days=time))        #date of checking into + days from time
    checkinto = ['Imię i nazwisko: %s \nNumer paszportu: %s \nData urodzenia: %s \nFirma: %s \nNumer pokoju: %s' 
                '\nData zameldowania: %s \nZostaje do: %s \nKwota: %szł\n' % (c.name, c.passport, c.birth, c.company,
                                                                              room, str(date), checkout, str(r.amount))]

    with open('meldunki.txt', 'a') as f:
        for linia in checkinto:
            f.write(linia + '\n')

elif decision == "2":
    name = input("Podaj imię i nazwisko: ")
    hmany = int(input("Ile bagaży? "))
    luggage = ['Imię i nazwisko: %s\nIlość bagaży: %s\nKiedy zostawiono: %s\n' % (name, str(hmany), str(date))]
    with open('bagaze.txt', 'a') as f:
        for linia in luggage:
            f.write(linia + '\n')                                      #saving to bagaze.txt
elif decision == "3":
    hmanywashes = int(input("Ile prań? "))                                  #just calculator
elif decision == "4":
    registrationnumb = input("Podaj numer rejestracjny: ")
    name = input("Podaj imię i nazwisko: ")
    car = ['Imię i nazwisko: %s\nNumer rejestracyjny: %s\n Kiedy zostawiono: %s\n' % (name, registrationnumb, str(date))]
    with open('samochod.txt', 'a') as f:
        for linia in car:
            f.write(linia + '\n')                                      #saving to samochod.txt
elif decision == "0":                          # if room is not in database - roomcreator
    createordelete = input("Jeśli chcesz stworzyć pokój, wyślij: s\nJeśli chcesz usunąć pokój wyślij: u")
    if createordelete == 's':
        r.roomcreator()
    elif createordelete == 'u':
        r.roomdata()
        roomtodelete = int(input("Iluosobowy pokój chcesz usunąć?"))
        r.roomdelete()
else:
    print("Błąd4")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
