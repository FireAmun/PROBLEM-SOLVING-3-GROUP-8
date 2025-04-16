class OrderSystem:
    def __init__(self):
        self.menu = {
            1: {"name": "Burger", "price": 10},
            2: {"name": "Pizza", "price": 20},
            3: {"name": "Fries", "price": 5}
        }
        self.cart = []
        self.user_logged_in = True
        self.status = "Not Ordered"

    def display_menu(self):
        print("Menu:")
        for item_id, item in self.menu.items():
            print(f"{item_id}: {item['name']} - RM{item['price']}")

    def add_to_cart(self, item_id, quantity):
        # === Assertion: Pre-condition checks ===
        assert self.user_logged_in, "User must be logged in"
        assert item_id in self.menu, "Item ID must be valid"
        assert quantity > 0, "Quantity must be greater than 0"

        item = self.menu[item_id]
        self.cart.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": quantity
        })

        # === Invariant: All cart quantities must remain positive ===
        for i in self.cart:
            assert i["quantity"] > 0, "Invariant failed: Quantity must stay positive"

    def place_order(self):
        # === Assertion: Pre-condition ===
        assert len(self.cart) > 0, "Cannot place order with empty cart"

        total = sum(i["price"] * i["quantity"] for i in self.cart)

        # === Invariant: Total must always be >= 0 during processing ===
        assert total >= 0, "Invariant failed: Total price cannot be negative"

        self.status = "Order Placed"
        self.cart.clear()

        # === Assertion: Post-condition checks ===
        assert self.status == "Order Placed", "Order status must be updated"
        assert len(self.cart) == 0, "Cart must be empty after placing the order"

        return total


# === Run the Program ===
system = OrderSystem()
system.display_menu()

try:
    item_id = int(input("Enter the ID of the item you want to order: "))
    quantity = int(input("Enter the quantity: "))

    system.add_to_cart(item_id, quantity)
    total_amount = system.place_order()

    print("✅ Order placed successfully!")
    print(f"🧾 Total amount: RM{total_amount}")

except AssertionError as e:
    print(f"❌ Error: {e}")
except ValueError:
    print("❌ Please enter valid numbers for item ID and quantity.")
