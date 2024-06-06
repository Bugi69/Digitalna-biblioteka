class Book:
    def __init__(self, naziv, autor, god_izdanja, zanr):
        self.naziv = naziv
        self.autor = autor
        self.god_izdanja = god_izdanja
        self.zanr = zanr
        
    def display_info(self):
        return f'{self.naziv}, {self.autor}, {self.god_izdanja}, {self.zanr}'