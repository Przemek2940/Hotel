#! /home/przemek2940/PycharmProjects/venv00/bin python3
# -*- coding: utf-8 -*-

from datetime import date
import datetime
import sqlite3

def main(args):                                                        #program screen
    if decision == "1":
        print(name, "musi zapłacić", "tu powinna być funkcja " "złotych za meldunek.")
    if decision == "2":
        if hmany == 1:
            print(name, "zostawił", hmany, "bagaż, dnia:", date)
        elif hmany > 1 and hmany < 5:
            print(name, "zostawił", hmany, "bagaże", date)
        else:
            print(name, "zostawił", hmany, "bagaży", date)
    elif decision == "3":
        washingcost = hmanywashes * washing
        if hmanywashes == 1:
            print(hmanywashes, "pranie kosztować będzie", washingcost, "zł.")
        elif hmanywashes > 1 and hmanywashes < 5:
            print(hmanywashes, "prania kosztować będą", washingcost, "zł.")
        else:
            print(hmanywashes, "prań kosztować będzie", washingcost, "zł.")
    elif decision == "4":
        print(name, "zostawił auto o numerach rejestracyjnych: ", registrationnumb, ". Dnia: ", date)
    else:
        print("Błąd")


def roomdata():                                                   #prints available rooms
    con = sqlite3.connect('pokoje.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM room")
    results = cur.fetchall()
    for row in results:
        print("\nDostępne pokoje:")
        print(row[0], "osobowy pokój")
        print("Cena: ", row[1], "\n")


def roomcreator():
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


def roomdelete():
    con = sqlite3.connect('pokoje.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute(f"DELETE from room WHERE beds = '{roomtodelete}'")
    con.commit()
    exit()


def roomchecking():                                     # searching for room in database
    con = sqlite3.connect('pokoje.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if whichroom > 0:
        cur.execute(f"SELECT * from room WHERE beds='{whichroom}'")
        if cur.fetchall():
            return whichroom
        else:
            creatordecision = input("Nie ma takiego pokoju. Chcesz go stworzyć? (t/n)") #posibility to create a room
            if creatordecision == 't':
                roomcreator()
                roomdata()
                roomchecking()
            else:
                print("Błąd")
    elif whichroom == 0:                                            # what to dooooooo
        roomcreator()
        roomdata()
        cur.execute(f"SELECT * from room WHERE beds='{whichroom2}'")
        if cur.fetchall():
            return whichroom2
        else:
            print("Błąd")

def amount():
    con = sqlite3.connect('pokoje.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    if whichroom > 0:
        cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom}")
        results = cur.fetchall()
        for row in results:
            print(int(row[0]) * time)
    elif whichroom == 0:                                                # whichroom2 here too
        cur.execute(f"SELECT price, beds FROM room WHERE beds = {whichroom2}")
        results = cur.fetchall()
        for row in results:
            print(int(row[0]) * time)



decision = input("""Jeśli chcesz kogoś zameldować: wybierz 1.\nJeśli chcesz dodać bagaż: wybierz 2
Jeśli chcesz rozliczyć pralnię: wybierz 3\nJeśli chcesz rozliczyć postój samochodu: wybierz 4
Jeśli chcesz dodać lub usunąć pokój: wybierz 0\n""")
washing = 7
date = date.today()

if decision == "1":
    name = input("Podaj imię i nazwisko: ")
    passport = input("Podaj numer paszportu: ")
    birth = input("Podaj datę urodzenia: ")
    company = input("Jaka firma? ")
    roomdata()
    whichroom = int(input("Który pokój wybrać? \nJeśli chcesz stworzyć pokój: wybierz 0 \n"))
    if whichroom == 0:
        roomchecking()
        whichroom2 = int(input("Iluosobowy pokój chcesz stworzyć i wynająć? "))         #whichroom2 here too
    room = input("Numer pokoju: ")
    time = int(input("Ile dni?"))
    amount()
    checkout = str(date + datetime.timedelta(days=time))        #date of checking into + days from time
    checkinto = ['Imię i nazwisko: ' + name, 'Numer paszportu: ' + passport, 'Data urodzenia: ' + birth, 'Firma: ' +
            company, 'Numer pokoju: ' + room, 'Data zameldowania: ' + str(date), 'Zostaje do: ' + checkout,
            'Kwota: ' + str(amount) + 'zł', '\n']
    with open('meldunki.txt', 'a') as f:
        for linia in checkinto:
            f.write(linia + '\n')                                       #saving to meldunki.txt
elif decision == "2":
    name = input("Podaj imię i nazwisko: ")
    hmany = int(input("Ile bagaży? "))
    luggage = ['Imię i nazwisko: ' + name, 'Ilość bagaży: ' + str(hmany), 'Kiedy zostawiono: ' + str(date), '\n']
    with open('bagaze.txt', 'a') as f:
        for linia in luggage:
            f.write(linia + '\n')                                      #saving to bagaze.txt
elif decision == "3":
    hmanywashes = int(input("Ile prań? "))                                  #just calculator
elif decision == "4":
    registrationnumb = input("Podaj numer rejestracjny: ")
    name = input("Podaj imię i nazwisko: ")
    car = ['Imię i nazwisko: ' + name, "Numer rejestracyjny: ", registrationnumb, 'Kiedy zostawiono: ' + str(date), '\n']
    with open('samochod.txt', 'a') as f:
        for linia in car:
            f.write(linia + '\n')                                      #saving to samochod.txt
elif decision == "0":                          # if room is not in database - roomcreator
    createordelete = input("Jeśli chcesz stworzyć pokój, wyślij: s\nJeśli chcesz usunąć pokój wyślij: u")
    if createordelete == 's':
        roomcreator()
    elif createordelete == 'u':
        roomdata()
        roomtodelete = int(input("Iluosobowy pokój chcesz usunąć?"))
        roomdelete()
else:
    print("Błąd")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
