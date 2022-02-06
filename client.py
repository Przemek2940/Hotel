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
