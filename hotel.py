#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-
from datetime import *
import datetime
import sqlite3
import client
import luggage
c = client.Client()
l = luggage.Luggage()


class RoomManagement:
    @staticmethod
    def roomdata():  # prints available rooms
        con = sqlite3.connect('pokoje.db')
        cur = con.cursor()
        cur.execute("SELECT * FROM room")
        results = cur.fetchall()
        print("Dostępne pokoje:\n")
        for row in results:
            print("%s-osobowy pokój.\nCena: %szł\n" % (row[0], row[1]))

    @staticmethod
    def roomcreator():
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS room (
                beds INTEGER PRIMARY KEY ASC,
                price varchar(250) DEFAULT ''
            )""")

        cur.execute("""
        INSERT OR IGNORE INTO room (beds, price)
        VALUES (?,?)
        """, (nbeds, nprice))
        con.commit()

    @staticmethod
    def roomdelete():
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(f"DELETE from room WHERE beds = '{roomtodelete}'")
        con.commit()
        exit()

    @staticmethod
    def roomchecking():  # searching for room in database
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

    @staticmethod
    def amount():
        con = sqlite3.connect('pokoje.db')
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        if whichroom > 0:
            cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom}")
            results = cur.fetchall()
            for row in results:
                return int(row[0]) * time
        elif whichroom == 0:  # whichroom2 here too
            cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom2}")
            results = cur.fetchall()
            for row in results:
                return int(row[0]) * time


def main():                                                        # program screen
    if decision == "1":
        print("%s musi zapłacić %s złotych za meldunek" % (c.name, r.amount()))
    if decision == "2":
        if l.hmany == 1:
            print("%s zostawił %s bagaż, dnia: %s" % (l.name, l.hmany, date))
        elif 5 > l.hmany > 1:
            print("%s zostawił %s bagaże, dnia: %s" % (l.name, l.hmany, date))
        else:
            print("%s zostawił %s bagaży, dnia %s" % (l.name, l.hmany, date))
    elif decision == "3":
        washingcost = hmanywashes * washing
        if hmanywashes == 1:
            print("%s pranie kosztować będzie %szł" % (hmanywashes, washingcost))
        elif 5 > hmanywashes > 1:
            print("%s prania kosztować będą %szł." % (hmanywashes, washingcost))
        else:
            print("%s prań kosztować będzie %szł." % (hmanywashes, washingcost))
    elif decision == "4":
        print("%s zostawił auto o numerach rejestracyjnych: %s. Dnia: %s" % (name, registrationnumb, date))


washing = 7
date = date.today()
timehr = datetime.datetime.now()
r = RoomManagement()

while True:
    print("\n" + "x" * 40 + "\n")
    decision = input("""Meldowanie: wybierz 1.\nBagaże: wybierz 2\nPralnia: wybierz 3
Postój samochodu: wybierz 4\nJeśli chcesz dodać lub usunąć pokój: wybierz 0\nJeśli chcesz zakonczyć: wybierz x\n""")

    if decision == "1":
        c.inputuserdata()
        r.roomdata()
        c.clientdb()
        whichroom = int(input("Który pokój wybrać? \nJeśli chcesz stworzyć pokój: wybierz 0 \n"))
        if whichroom == 0:
            whichroom2 = int(input("Iluosobowy pokój chcesz stworzyć? "))
            nprice = input("Jaka będzie cena za osobę? ")
            nbeds = whichroom2
            r.roomchecking()
            print("Wybrany pokój: %s-osobowy" % whichroom2)
        else:
            r.roomchecking()
        room = input("Numer pokoju: ")
        time = int(input("Ile dni?"))
        checkout = str(date + datetime.timedelta(days=time))        # date of checking into + days from time
        checkinto = ['Imię i nazwisko: %s \nNumer paszportu: %s \nData urodzenia: %s \nFirma: %s \nNumer pokoju: %s' 
                     '\nData zameldowania: %s \nZostaje do: %s \nKwota: %szł\n' % (c.name, c.passport, c.birth,
                                                                                   c.company, room, str(date), checkout,
                                                                                   str(r.amount()))]
        with open('meldunki.txt', 'a') as f:
            for linia in checkinto:
                f.write(linia + '\n')

    elif decision == "2":
        whattodo = input("Dodanie bagażu: Wybierz 1\nOdebranie bagażu: Wybierz 2\n")
        if whattodo == '1':                                         # luggage class teleport
            l.inputluggage()
            l.txtsaving()
            l.dbsaving()
    elif decision == "3":
        hmanywashes = int(input("Ile prań? "))
        roomnumber = input("Numer pokoju: ")
        washes = ['Data i godzina prania: %s:%s, %s, Pokój: %s' % (timehr.hour, timehr.minute, date, roomnumber)]
        with open('pranie.txt', 'a') as f:
            for linia in washes:
                f.write(linia + '\n')
    elif decision == "4":
        registrationnumb = input("Podaj numer rejestracjny: ")
        name = input("Podaj imię i nazwisko: ")
        car = ['Imię i nazwisko: %s\nNumer rejestracyjny: %s\nZostawiono dnia: %s\n' % (name, registrationnumb,
                                                                                        str(date))]
        with open('samochod.txt', 'a') as f:
            for linia in car:
                f.write(linia + '\n')                                      # saving to samochod.txt
    elif decision == "0":                          # if room is not in database - roomcreator
        createordelete = input("Jeśli chcesz stworzyć pokój, wyślij: s\nJeśli chcesz usunąć pokój wyślij: u\n")
        if createordelete == 's':
            nbeds = input("Iluosobowy pokój chcesz stworzyć?")
            nprice = input("Jaka będzie cena za osobę? ")
            r.roomcreator()
            print("Nowy stan pokoi:")
            r.roomdata()
        elif createordelete == 'u':
            r.roomdata()
            roomtodelete = int(input("Iluosobowy pokój chcesz usunąć?"))
            r.roomdelete()
    elif decision == "x":
        break
    else:
        print("Błąd4")

    if __name__ == '__main__':
        main()
exit()
