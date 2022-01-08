#! /home/przemek2940/Python/bin python3
# -*- coding: utf-8 -*-

from datetime import date
import datetime

decyzja = input("""Jeśli chcesz kogoś zameldować: wybierz 1.\nJeśli chcesz dodać bagaż: wybierz 2
Jeśli chcesz rozliczyć pralnię: wybierz 3\nJeśli chcesz rozliczyć postój samochodu: wybierz 4\n""")
pokoj4 = 35
pokoj3 = 42
pokoj2 = 48
pokoj1 = 60
pranie = 7


if decyzja == "1":
    imie = input("Podaj imię i nazwisko: ")
    paszport = input("Podaj numer paszportu: ")
    dataur = input("Podaj datę urodzenia: ")
    firma = input("Jaka firma?")
    ileos = input("Iluosobowy pokój?")
    pokoj = input("Numer pokoju: ")
    czas = int(input("Ile dni?"))
    data = date.today()
    datawymeldowania = str(data + datetime.timedelta(days=czas))
    dane = ['Imię i nazwisko: ', imie, 'Numer paszportu: ', paszport, 'Data urodzenia: ', dataur, 'Firma: ',
            firma,'Numer pokoju: ', pokoj, 'Data zameldowania: ', str(data), 'Zostaje do: ', datawymeldowania, '\n']
    with open('meldunki.txt', 'a') as f:
        for linia in dane:
            f.write(linia + '\n')
elif decyzja == "2":
    imie = input("Podaj imię i nazwisko: ")
    ile = int(input("Ile bagaży? "))
elif decyzja == "3":
    ilepran = int(input("Ile prań? "))
elif decyzja == "4":
    rejestracja = input("Podaj numer rejestracjny: ")
    imie = input("Podaj imię i nazwisko: ")
else:
    print("Błąd")


def cena():
    if ileos == "4":
        kwota = czas * pokoj4
    elif ileos == "3":
        kwota = czas * pokoj3
    elif ileos == "2":
        kwota = czas * pokoj2
    elif ileos == "1":
        kwota = czas * pokoj1
        print("Błąd.")
    return kwota


def main(args):
    if decyzja == "1":
        print(imie, "musi zapłacić", cena(), "złotych za meldunek.")
    elif decyzja == "2":
        if ile == 1:
            print(imie, "zostawił", ile, "bagaż, dnia:", date.today())
        elif ile > 1 and ile < 5:
            print(imie, "zostawił", ile, "bagaże", date.today())
        else:
            print(imie, "zostawił", ile, "bagaży", date.today())
    elif decyzja == "3":
        kosztprania = ilepran * pranie
        if ilepran == 1:
            print(ilepran, "pranie kosztować będzie", kosztprania, "zł.")
        elif ilepran > 1 and ilepran < 5:
            print(ilepran, "prania kosztować będą", kosztprania, "zł.")
        else:
            print(ilepran, "prań kosztować będzie", kosztprania, "zł.")
    elif decyzja == "4":
        print(imie, "zostawił auto o numerach rejestracyjnych: ", rejestracja, ". Dnia: ", date.today())
    else:
        print("Błąd")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
