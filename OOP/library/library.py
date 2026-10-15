import random
class Library:
    def __init__(self, address, members, books):
        self.address = address
        self.members = members
        self.books = books

    # Shows available books
    def availableBooks(self):
        for book in self.books:
            if not book.borrowed:
                print(book.name + " " + str(book.isbn))

    # Shows members
    def showMembers(self):
        [print(member.name + " " + str(member.id)) for member in self.members]
    def addMember(self, new_member):
        self.members.append(new_member)
        print(f"New member added: {new_member}")
    def removeMembers(self, id):
        if id in self.members:
            self.members.remove(id)
        else:
            print("member doesnt exist")

class Member:
    def __init__(self, name, books, ID):
        self.name = name
        self.id = ID
        self.books = books
        # libobj.members.append([self.id, self.name])
    
    # Takes a obj, checks if 
    def member_borrow(self, book):
        if book.book_borrow():
            self.books.append(book)
        else:
            print("not available")
    def displayBooks(self):
        [print(book.name) for book in self.books]

class Book:
    def __init__(self, name, author, borrowed, isbn):
        self.name = name
        self.author = author
        self.borrowed = borrowed
        self.isbn = isbn
    def book_borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print("Book is now borrowed.")
            return True
        else:
            return False

    def returnBook(self):
        if self.borrowed:
            self.borrowed = False


# Test part

test_book = Book("test", "test", False, 16637)
test_book2 = Book("test2", "test2", True, 4567898765432)
bob = Member("Bob", [], 1)
alice = Member("alice", [], 2)

member_list = [bob, alice]
test_library=Library("test st", member_list, [test_book, test_book2])

#bob.member_borrow(test_book)
#alice.member_borrow(test_book2)
test_library.availableBooks()
test_library.showMembers()
