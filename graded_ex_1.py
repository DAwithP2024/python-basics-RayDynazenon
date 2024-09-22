
# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}


def display_sorted_products(products_list, sort_order):
    if sort_order == "asc":
        return sorted(products_list, key=lambda x: x[1])
    elif sort_order == "desc":
        return sorted(products_list, key=lambda x: x[1], reverse=True)

def display_products(products_list):
    for index, product in enumerate(products_list):
        print(f"{index + 1}. {product[0]} - ${product[1]}")

def display_categories():
    for index, category in enumerate(products):
        print(f"{index + 1}. {category}")
    choice = input("Select a category by number: ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= len(products):
            return choice - 1
    return None


def add_to_cart(cart, product, quantity):
    cart.append((product[0], product[1], quantity))

def display_cart(cart):
    total_cost = 0
    output = ""
    for item in cart:
        product_name, product_price, quantity = item
        total_cost += product_price * quantity
        output += f"{product_name} - ${product_price} x {quantity} = ${product_price * quantity}\n"
    output += f"Total cost: ${total_cost}"
    
    print(output)
    return output

def total_cost(cart):
    total_cost = 0
    for item in cart:
        product_name, product_price, quantity = item
        total_cost += product_price * quantity

    return total_cost

def generate_receipt(name, email, cart, total_cost, address):
    print(f"Customer: {name}\nEmail: {email}\nItems Purchased:\n")
    for product_name, product_price, quantity in cart:
        print(f"{product_name} - ${product_price} x {quantity} = ${product_price * quantity}")
    print(f"Total: ${total_cost}\nDelivery Address: {address}\nYour items will be delivered in 3 days.\nPayment will be accepted upon delivery.")

def validate_name(name):
    if " " in name:
        words = name.split()
        for word in words:
            if not word.isalpha():
                return False
        return True

def validate_email(email):
    return "@" in email and not " " in email

def main():
    category_index = display_categories()
    if category_index is not None:
        category = list(products.keys())[category_index]
        display_products(products[category])
        product_choice = input("Select a product by number: ")
        if product_choice.isdigit():
            product_choice = int(product_choice) - 1
            if 0 <= product_choice < len(products[category]):
                quantity = input("Enter quantity: ")
                if quantity.isdigit() and int(quantity) > 0:
                    quantity = int(quantity)
                    cart = []
                    add_to_cart(cart, products[category][product_choice], quantity)
                    display_cart(cart)
                else:
                    print("Invalid quantity. Please enter a positive number.")
                    return None
            else:
                print("Invalid product choice. Please select a valid product.")
                return None
        else:
            print("Invalid product number. Please enter a valid number.")
            return None
    else:
        print("Invalid category choice. Please select a valid category.")
        return None

    return category_index


""" The following block makes sure that the main() function is called when the program is run. 
It also checks that this is the module that's being run directly, and not being used as a module in some other program. 
In that case, only the part that's needed will be executed and not the entire program """
if __name__ == "__main__":
    main() 
