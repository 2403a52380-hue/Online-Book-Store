BOOKS = [
    {"id": 1, "title": "Python Basics", "price": 400},
    {"id": 2, "title": "Web Development", "price": 500},
    {"id": 3, "title": "Data Structures", "price": 450},
]


def display_books():
    for book in BOOKS:
        print(book["id"], book["title"], book["price"])


def search_books(keyword):
    return [
        book for book in BOOKS
        if keyword.lower() in book["title"].lower()
    ]
def get_book_by_id(book_id):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return None