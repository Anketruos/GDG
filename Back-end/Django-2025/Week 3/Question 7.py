class Library():
    books = []
    def add_book(self, *args):
        for book in args:
            self.books.append(book)
    def show_book(self):
        for i in range(len(self.books)):
            print(self.books[i])

l1 = Library()
l1.add_book('english', 'herry potter')
l1.show_book()