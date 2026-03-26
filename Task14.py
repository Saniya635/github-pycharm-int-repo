#lab assignment 1
class Employee:
    def __init__(self, name, age, salary, address):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)
class Manager(Employee):
    def __init__(self, name, age, salary, address):
        super().__init__(name, age, salary, address)
managers = []
for i in range(3):
    print(f"\nEnter details of Manager {i+1}")
    name = input("Name: ")
    age = int(input("Age: "))
    salary = int(input("Salary: "))
    address = input("Address: ")
    m = Manager(name, age, salary, address)
    managers.append(m)
print("\nManager Details:")
for m in managers:
    m.display()

#lab assignment 2
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True
class Member:
    def __init__(self, name):
        self.name = name

class Library:
    def __init__(self):
        self.books = []
    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added.")
    def display_books(self):
        for b in self.books:
            print(b.title, "-", "Available" if b.available else "Issued")
    def lend_book(self, title):
        for b in self.books:
            if b.title == title and b.available:
                b.available = False
                print("Book issued.")
                return
        print("Book not available.")
    def return_book(self, title):
        for b in self.books:
            if b.title == title:
                b.available = True
                print("Book returned.")

lib = Library()
while True:
    print("\n1.Add 2.Display 3.Lend 4.Return 5.Exit")
    ch = int(input("Enter choice: "))
    if ch == 1:
        title = input("Enter book name: ")
        lib.add_book(title)
    elif ch == 2:
        lib.display_books()
    elif ch == 3:
        title = input("Enter book to lend: ")
        lib.lend_book(title)
    elif ch == 4:
        title = input("Enter book to return: ")
        lib.return_book(title)
    else:
        break