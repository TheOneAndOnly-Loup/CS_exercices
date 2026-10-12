import random
class Library:
    def __init__(self, address, members, books):
        self.address = address
        self.members = members
        self.books = books
    def availableBooks(self):
        print(f"Available books: {self.books}")
    def showMembers(self):
        print(f"Library members: {self.members}")
    def addMembers(self, new_member):
        self.members.append(new_member)
        print(f"New member added: {new_member}")
    def removeMembers(self, name):
        self.members.remove(name)

class Member:
    def __init__(self, name, books):
        self.name = name
        self.ID = random.randint(0, 10)
        self.books = books
    def borrow(self, book):
        self.books.append(book)
        book.updateStatus()

class Book:
    def __init__(self, name, author, borrowed, isbn):
        self.name = name
        self.author = author
        self.borrowed = borrowed
        self.isbn = isbn
    def updateStatus(self):
        self.borrowed = not self.borrowed
        print("Borrowed status has been flipped.")



    