class Book:
    def __init__(self, title, author,):
        self.title = title
        self.author = author
        self.is_borrowed = False
    
    def borrow(self):
        self.is_borrowed = True
        print("The book", self.title, "has been borrowed")
    
    def  return_book(self):
        self.is_borrowed = False
        print("The book", self.title,"returned")

Book_1 = ("Diary of a wimpy kid", "Jeff Kinney")
Book_2 = ("Harry Potter", "J.K Rowling")
Book_3 = ("Rowleys Adventures", "Jeff Kinney")


Book_1.borrow()
Book_1.return_book()

Book_2.borrow()
Book_2.return_book()

Book_3.borrow()
Book_3.return_book()

