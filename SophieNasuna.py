# Class 1
class Book:
    # Constructor method
    # Runs automatically when an object is created
    def __init__(self, title, pages, author, year, publisher):
        self.title = title
        self.pages = pages
        self.author = author
        self.year = year
        self.publisher = publisher

def display_info(self):
    print(f"{self.title}, {self.author}, ({self.year})")    

def is_classic(self):
    if 2026 - self.year > 20:
        print(self.title, "Is a classic book")    
    else:
        print(self.title, "Is a modern book")
    

book1 = Book('Atomic Habits', 1, 'James Clear', 2018, 'Arthur')
book2 = Book('Sapiens', 3, 'Yuval Noah Harari', 2003, 'John')
book3 = Book('1984', 5, 'George Orwell', 2001, 'Peter')
book4 = Book('Jack and Jill', 8, 'Jonah', 1999, 'Aaron')
book5 = Book('Dune', 90, 'Frank Herbert', 1987, 'Christopher')  


# Class 2
class BankAccount:
    # Constructor method
    def __init__(self, account_number, owner, balance, bank_name, currency):
        self.account_number = account_number  
        self.owner = owner                    
        self.balance = balance                 
        self.bank_name = bank_name             
        self.currency = currency               

    # Method to add money into account
    def deposit(self, amount):
        self.balance += amount

    # Method to display account details
    def display_info(self):
        print(f"{self.owner} - Balance: {self.balance} {self.currency}")


# Creating 5 BankAccount objects
acc1 = BankAccount("001", "Alice", 500, "Equity", "UGX")
acc2 = BankAccount("002", "Brian", 800, "Stanbic", "UGX")
acc3 = BankAccount("003", "Cathy", 1200, "DFCU", "UGX")
acc4 = BankAccount("004", "David", 300, "Centenary", "UGX")
acc5 = BankAccount("005", "Eva", 950, "Absa", "UGX")


# Class 3
class OnlineCourse:
    # Constructor initializes course details
    def __init__(self, title, instructor, duration, platform, price):
        self.title = title          
        self.instructor = instructor 
        self.duration = duration     
        self.platform = platform    
        self.price = price          

    # Method to apply discount to course price
    def discount(self, percent):
        self.price -= self.price * percent / 100

    # Method to display course details
    def show_course(self):
        print(f"{self.title} by {self.instructor} - {self.price} USD")


# Creating 5 OnlineCourse objects
course1 = OnlineCourse("Python Basics", "John", 10, "Udemy", 50)
course2 = OnlineCourse("Web Dev", "Mary", 15, "Coursera", 80)
course3 = OnlineCourse("Cyber Security", "James", 20, "edX", 100)
course4 = OnlineCourse("Data Science", "Linda", 25, "Udacity", 120)
course5 = OnlineCourse("AI Intro", "Peter", 18, "FutureLearn", 90)


# Class 4
class SmartDevice:

    # Constructor sets device details
    def __init__(self, brand, model, battery, storage, is_on):
        self.brand = brand       
        self.model = model       
        self.battery = battery  
        self.storage = storage   
        self.is_on = is_on       

    # Method to turn device ON
    def power_on(self):
        self.is_on = True

    # Method to turn device OFF
    def power_off(self):
        self.is_on = False


# Creating 5 SmartDevice objects
device1 = SmartDevice("Samsung", "S21", 80, "128GB", False)
device2 = SmartDevice("Apple", "iPhone 13", 70, "256GB", False)
device3 = SmartDevice("Huawei", "P40", 60, "128GB", False)
device4 = SmartDevice("Xiaomi", "Mi 11", 90, "256GB", False)
device5 = SmartDevice("Google", "Pixel 7", 85, "128GB", False)


# Class 5
class EventTicket:
    # Constructor 
    def __init__(self, event_name, holder, seat_number, price, valid):
        self.event_name = event_name     
        self.holder = holder            
        self.seat_number = seat_number  
        self.price = price              
        self.valid = valid              

    # Method to use ticket 
    def use_ticket(self):
        self.valid = False

    # Method to display ticket details
    def show_ticket(self):
        print(f"{self.event_name} - Seat {self.seat_number} - {self.holder}")


# Creating 5 EventTicket objects
ticket1 = EventTicket("Concert", "Alice", "A1", 100, True)
ticket2 = EventTicket("Conference", "Brian", "B2", 150, True)
ticket3 = EventTicket("Seminar", "Cathy", "C3", 80, True)
ticket4 = EventTicket("Festival", "David", "D4", 120, True)
ticket5 = EventTicket("Workshop", "Eva", "E5", 60, True)


