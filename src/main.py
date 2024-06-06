from library import Library
from book import Book
libary = Library()

unos = input("Zdravo! Izaberite akciju koju zelite da izvrsite (1-Dodavanje knjige, 2-Brisanje knjige, 3-Menjanje informacija o knjigama, 4-Prikaz svih knjiga): ")
if unos =="1":
    while True:
        print("Napisite informacije o knjizi.")
        naziv = input("Naziv: ")
        autor = input("Autor: ")
        god_izdanja = input("Godina izdanja: ")
        zanr = input("Zanr: ")
        book = Book(naziv, autor, god_izdanja, zanr)
        libary.dodaj_knjigu(book)
        code = input("Ako zelite da prekinete upis knjiga unesite 0 ")
        if code == "0":
            break
    
    with open("fajl.txt", "a") as file:
        for object in libary.lista_objekata:
            file.write(object.display_info() + "\n")
elif unos == "2":
    print("Napisite informacije o knjizi koju zelite da izbrisete.")
    naziv = input("Naziv: ")
    autor = input("Autor: ")
    god_izdanja = input("Godina izdanja: ")
    zanr = input("Zanr: ")
    book = Book(naziv, autor, god_izdanja, zanr)
    with open("fajl.txt", "r") as file:
        lines = file.readlines()
    with open("fajl.txt", "w") as file:
        for line in lines:
            if line.strip() != book.display_info().strip():
                file.write(line)
