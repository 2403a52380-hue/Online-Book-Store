
from books import display_books, search_books
from cart import add_to_cart
from customer import customer_info


def main():
    print("=== Online Book Store ===")

    display_books()
    search_books("Python")

    cart = []
    add_to_cart(cart, 1)
    print("Cart:", cart)

    print(customer_info("Alex", "alex@example.com"))


if __name__ == "__main__":
    main()
