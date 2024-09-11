class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price:.2f}")

    def apply_discount(self, discount_percentage):
        self.price -= self.price * (discount_percentage / 100)

# Example usage:
book1 = Book("To Kill a Mockingbird", "Harper Lee", 29.99)
book2 = Book("1984", "George Orwell", 24.99)

print("Details of Book 1:")
book1.display_details()

print("\nDetails of Book 2:")
book2.display_details()

# Apply a 10% discount to book2
book2.apply_discount(10)
print("\nDetails of Book 2 after applying a 10% discount:")
book2.display_details()
