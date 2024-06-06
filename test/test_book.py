import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from book import Book

class Test_Book(unittest.TestCase):
    def test_dodavanje_naslova(self):
        b= Book("Necista krv","Borislav Stankovic", 1910,"Drama")
        self.assertEqual(b.naziv,"Necista krv")
        
    def test_dodavanje_autora(self):
        b= Book("Necista krv","Borislav Stankovic", 1910,"Drama")    
        self.assertEqual(b.autor, "Borislav Stankovic")

    def test_dodavanje_godine(self):
        b= Book("Necista krv","Borislav Stankovic", 1910,"Drama")
        self.assertEqual(b.god_izdanja, 1910)

    def test_dodavanje_zanra(self):
        b= Book("Necista krv","Borislav Stankovic", 1910,"Drama")    
        self.assertEqual(b.zanr, "Drama")

    def test_displayinfo(self):
        b = Book("d", "d", 1954, "d")
        self.assertEqual(b.display_info(), "d, d, 1954, d")  

if __name__ == '__main__':
   unittest.main()
