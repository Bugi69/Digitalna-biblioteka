class Library:
    def __init__(self):
        self.lista_objekata = []
    
    def dodaj_knjigu(self, book):
        self.lista_objekata.append(book)
        
    def ispis_knjiga(self):
        for object in self.lista_objekata:
            print(object.display_info())
    
    def search_books(self, search_criteria, keyword):
        results = []
        with open("fajl.txt", "r") as file:
            for line in file:
                book_data = line.strip().split(", ")
                if search_criteria.lower() == "naslov" and keyword.lower() in book_data[0].lower():
                    results.append(book_data)
                elif search_criteria.lower() == "autor" and keyword.lower() in book_data[1].lower():
                    results.append(book_data)
                elif search_criteria.lower() == "godina" and keyword == book_data[2]:
                    results.append(book_data)
                elif search_criteria.lower() == "zanr" and keyword.lower() in book_data[3].lower():
                    results.append(book_data)
        return results