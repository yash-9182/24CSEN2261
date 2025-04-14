# Product catalog (Product name: price)
products = {
    1: {"name": "Laptop", "price": 50000},
    2: {"name": "Smartphone", "price": 20000},
    3: {"name": "Headphones", "price": 2000},
    4: {"name": "Backpack", "price": 1500},
    5: {"name": "Smartwatch", "price": 3000}
}

# Shopping cart
cart = []

def display_products():
    print("\n--- Product Catalog ---")
    for pid, item in products.items():
        print(f"{pid}. {item['name']} - ₹{item['price']}")

def add_to_cart():
    try:
        product_id = int(input("Enter the product number to add to cart: "))
        if product_id in products:
            cart.append(products[product_id])
            print(f"{products[product_id]['name']} added to cart.")
        else:
            print("Invalid product ID.")
    except ValueError:
        print("Please enter a valid number.")

def view_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("\n--- Your Cart ---")
    total = 0
    for index, item in enumerate(cart, 1):
        print(f"{index}. {item['name']} - ₹{item['price']}")
        total += item['price']
    print(f"Total Amount: ₹{total}")

def checkout():
    if not cart:
        print("Your cart is empty. Add items before checkout.")
        return
    view_cart()
    confirm = input("Do you want to place the order? (yes/no): ").lower()
    if confirm == 'yes':
        print("Order placed successfully! Thank you for shopping.")
        cart.clear()
    else:
        print("Checkout cancelled.")

def show_menu():
    print("\n--- eCommerce Store Menu ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

# Main loop
while True:
    show_menu()
    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 1:
        display_products()
    elif choice == 2:
        add_to_cart()
    elif choice == 3:
        view_cart()
    elif choice == 4:
        checkout()
    elif choice == 5:
        print("Thank you for visiting! Goodbye.")
        break
    else:
        print("Invalid choice. Please t
