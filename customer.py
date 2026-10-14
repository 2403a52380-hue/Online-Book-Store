def customer_info(name, email):
    return f"Customer: {name}, Email: {email}"
def customer_info(name, email):
    return {
        "name": name,
        "email": email
    }


def display_customer(customer):
    print("Customer Name:", customer["name"])
    print("Customer Email:", customer["email"])