#! /home/przemek2940/Python/bin python3
# -*- coding: utf-8 -*-

from datetime import date

decyzja = input("""Jeśli chcesz kogoś zameldować: wybierz 1.\nJeśli chcesz dodać bagaż: wybierz 2
Jeśli chcesz rozliczyć pralnię: wybierz 3\n""")
pokoj4 = 35
pokoj3 = 42
pokoj2 = 48
pokoj1 = 60
pranie = 7

if decyzja == "1":
    imie = input("Podaj imię i nazwisko: ")
    firma = input("Jaka firma?")
    pokoj = input("Iluosobowy pokój?")
    czas = int(input("Ile dni?"))
elif decyzja == "2":
    imie = input("Podaj imię i nazwisko: ")
    ile = int(input("Ile bagaży? "))
elif decyzja == "3":
    ilepran = int(input("Ile prań? "))
else:
    print("Błąd")


def cena():
    if pokoj == "4":
        kwota = czas * pokoj4
    elif pokoj == "3":
        kwota = czas * pokoj3
    elif pokoj == "2":
        kwota = czas * pokoj2
    elif pokoj == "1":
        kwota = czas * pokoj1
        print("Błąd.")
    return kwota


def main(args):
    kosztprania = ilepran * pranie
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
        if ilepran == 1:
            print(ilepran, "pranie kosztować będzie", kosztprania, "zł.")
        elif ilepran > 1 and ilepran < 5:
            print(ilepran, "prania kosztować będą", kosztprania, "zł.")
        else:
            print(ilepran, "prań kosztować będzie", kosztprania, "zł.")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
