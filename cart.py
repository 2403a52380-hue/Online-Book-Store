from books import BOOKS


def add_to_cart(cart, book_id):
    for book in BOOKS:
        if book["id"] == book_id:
            cart.append(book)
            return True
    return False