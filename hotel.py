#! /home/przemek2940/Python/bin python3
# -*- coding: utf-8 -*-

from datetime import date
import datetime
import json

def main(args):                                                        #program screen
    if decision == "1":
        print(name, "musi zapłacić", amount, "złotych za meldunek.")
    elif decision == "2":
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


decision = input("""Jeśli chcesz kogoś zameldować: wybierz 1.\nJeśli chcesz dodać bagaż: wybierz 2
Jeśli chcesz rozliczyć pralnię: wybierz 3\nJeśli chcesz rozliczyć postój samochodu: wybierz 4\n""")
washing = 7
date = date.today()

if decision == "1":
    name = input("Podaj imię i nazwisko: ")
    passport = input("Podaj numer paszportu: ")
    birth = input("Podaj datę urodzenia: ")
    company = input("Jaka firma?")
    beds = input("Iluosobowy pokój?")
    price = int(input("Jaka jest cena za pokój?"))
    obj = dict()                                                    #json
    obj[beds] = price
    plik = open('rooms.json', encoding='utf-8', mode="w")
    json.dump(obj, plik)
    plik.close()
    room = input("Numer pokoju: ")
    time = int(input("Ile dni?"))
    amount = price * time
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
else:
    print("Błąd")

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
