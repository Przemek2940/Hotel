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
data = date.today()

def cena():
    if ileos == "4":
        kwota = czas * pokoj4
    elif ileos == "3":
        kwota = czas * pokoj3
    elif ileos == "2":
        kwota = czas * pokoj2
    elif ileos == "1":
        kwota = czas * pokoj1
    return kwota


if decyzja == "1":
    imie = input("Podaj imię i nazwisko: ")
    paszport = input("Podaj numer paszportu: ")
    dataur = input("Podaj datę urodzenia: ")
    firma = input("Jaka firma?")
    ileos = input("Iluosobowy pokój?")
    pokoj = input("Numer pokoju: ")
    czas = int(input("Ile dni?"))
    datawymeldowania = str(data + datetime.timedelta(days=czas))        #dodaje do daty zameldowania dni z czas
    danemel = ['Imię i nazwisko: ' + imie, 'Numer paszportu: ' + paszport, 'Data urodzenia: ' + dataur, 'Firma: ' +
            firma, 'Numer pokoju: ' + pokoj, 'Data zameldowania: ' + str(data), 'Zostaje do: ' + datawymeldowania,
            'Kwota: ' + str(cena()) + 'zł', '\n']
    with open('meldunki.txt', 'a') as f:
        for linia in danemel:
            f.write(linia + '\n')                                       #zapisywanie do pliku meldunki.txt
elif decyzja == "2":
    imie = input("Podaj imię i nazwisko: ")
    ile = int(input("Ile bagaży? "))
    danebag = ['Imię i nazwisko: ' + imie, 'Ilość bagaży: ' + str(ile), 'Kiedy zostawiono: ' + str(data), '\n']
    with open('bagaze.txt', 'a') as f:
        for linia in danebag:
            f.write(linia + '\n')                                      #zapisywanie do pliku bagaze.txt
elif decyzja == "3":
    ilepran = int(input("Ile prań? "))                                  #nie ma potrzeby zapisywania, to tylko kalkulator
elif decyzja == "4":
    rejestracja = input("Podaj numer rejestracjny: ")
    imie = input("Podaj imię i nazwisko: ")
    danesam = ['Imię i nazwisko: ' + imie, "Numer rejestracyjny: ", rejestracja, 'Kiedy zostawiono: ' + str(data), '\n']
    with open('samochod.txt', 'a') as f:
        for linia in danesam:
            f.write(linia + '\n')                                      #zapisywanie do pliku samochod.txt
else:
    print("Błąd")


def main(args):                                                        #informacje pokazujące się w programie
    if decyzja == "1":
        print(imie, "musi zapłacić", cena(), "złotych za meldunek.")
    elif decyzja == "2":
        if ile == 1:
            print(imie, "zostawił", ile, "bagaż, dnia:", data)
        elif ile > 1 and ile < 5:
            print(imie, "zostawił", ile, "bagaże", data)
        else:
            print(imie, "zostawił", ile, "bagaży", data)
    elif decyzja == "3":
        kosztprania = ilepran * pranie
        if ilepran == 1:
            print(ilepran, "pranie kosztować będzie", kosztprania, "zł.")
        elif ilepran > 1 and ilepran < 5:
            print(ilepran, "prania kosztować będą", kosztprania, "zł.")
        else:
            print(ilepran, "prań kosztować będzie", kosztprania, "zł.")
    elif decyzja == "4":
        print(imie, "zostawił auto o numerach rejestracyjnych: ", rejestracja, ". Dnia: ", data)
    else:
        print("Błąd")


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
