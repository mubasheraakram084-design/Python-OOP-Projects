
class Book:

    def __init__(self, book_id, title, author, issued_to=None):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = issued_to

    def is_available(self):
        return self.issued_to is None

    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "issued_to": self.issued_to
        }
#to_dict() object ko JSON-compatible dictionary mein convert karta hai. from_dict() dictionary se Book object banata hai.
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["book_id"],
            data["title"],
            data["author"],
            data.get("issued_to")
        )
