
BOOKS = [
    {"id": 1, "title": "Python Basics", "price": 400},
    {"id": 2, "title": "Web Development", "price": 500},
    {"id": 3, "title": "Data Structures", "price": 450},
]


def display_books():
    for book in BOOKS:
        print(book["id"], book["title"], book["price"])


def get_book_by_id(book_id):
    for book in BOOKS:
        if book["id"] == book_id:
            return book
    return None


def search_books(keyword):
    keyword = keyword.strip().lower()

    if not keyword:
        return []

    return [
        book for book in BOOKS
        if keyword in book["title"].lower()
    ]
