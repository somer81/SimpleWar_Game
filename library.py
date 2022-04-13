class Library:
    pass

class Book:
    def __init__(self,name:str, author:str, numPage:int):
        self.__name = name
        self.__author = author
        self.__numPage = numPage

    def getName(self):
        return self.__name


class Person:
    def __init__(self, id: str, name: str, surname: str):
        self.__name = name
        self.__id = id
        self.__surname = surname




class Reader(Person):
    def __init__(self,id: str, name: str, surname: str):
        super().__init__(id, name, surname)
        self.__books = list()

    def borrowBook(self, book:Book):
        self.__books.append(book)

    def returnBook(self, book:Book):
        if self.__books:
            self.__books.remove(book)
        else:
            print("No books")

    def listBooks(self):
        if self.__books:
            for i in self.__books:
                print(i.getName())


class Officer(Person):
    def giveBook(self,book,reader:Reader):
        reader.borrowBook(book)

    def getBook(self, book, reader:Reader):
        reader.returnBook(book)


def Main():

    book1 = Book("Alice", "LAFontene",342)
    book2 = Book("Kuzu", "Masalci", 142)
    book3 = Book("PHP", "Edwin", 211)
    omer = Reader("123123","Omer","Sevinc")
    officer1 = Officer("123123","Pamir","Sevinc")

    omer.borrowBook(book1)
    omer.borrowBook(book2)
    omer.borrowBook(book3)

    omer.returnBook(book2)

    omer.listBooks()

if __name__ == "__main__":
    Main()