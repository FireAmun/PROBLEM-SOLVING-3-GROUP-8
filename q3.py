class FoodDeliveryApp:
    def __init__(self):
        self.menu = {
            1: {"name": "Nasi Lemak", "price": 8},
            2: {"name": "Mee Goreng", "price": 7},
            3: {"name": "Roti Canai", "price": 3},
            4: {"name": "Satay", "price": 10},
            5: {"name": "Teh Tarik", "price": 2}
        }
        self.cart = []
        self.orders = []

    def display_menu(self):
        print("🍽️  Malaysian Food Menu:")
        for item_id, item in self.menu.items():
            print(f"{item_id}: {item['name']} - RM{item['price']}")

    def add_to_cart(self, item_id, quantity):
        # === Pre-conditions ===
        assert item_id in self.menu, "❌ Item ID must be in the menu"
        assert quantity > 0, "❌ Quantity must be greater than 0"

        item = self.menu[item_id]
        self.cart.append({
            "item": item["name"],
            "price": item["price"],
            "quantity": quantity
        })

        # === Invariant ===
        for i in self.cart:
            assert i["quantity"] > 0, "❌ Invariant failed: quantity must stay positive"

    def checkout(self):
        # === Pre-condition ===
        assert len(self.cart) > 0, "❌ Cart cannot be empty before checkout"

        total = sum(i["price"] * i["quantity"] for i in self.cart)

        # === Invariant ===
        assert total >= 0, "❌ Invariant failed: total must be non-negative"

        order = {
            "items": self.cart.copy(),
            "total": total,
            "status": "Confirmed"
        }
        self.orders.append(order)
        self.cart.clear()

        # === Post-conditions ===
        assert self.orders[-1]["status"] == "Confirmed", "❌ Post-condition failed: order status must be confirmed"
        assert len(self.cart) == 0, "❌ Post-condition failed: cart must be empty after checkout"

        return order


# === Running the Program ===
app = FoodDeliveryApp()
app.display_menu()

try:
    item_id = int(input("🛒 Enter item ID to add to cart: "))
    quantity = int(input("🔢 Enter quantity: "))

    app.add_to_cart(item_id, quantity)

    print("🧾 Proceeding to checkout...")
    order = app.checkout()

    print("\n✅ Order Summary:")
    print("Items:", order["items"])
    print("Total: RM", order["total"])
    print("Status:", order["status"])

except AssertionError as e:
    print(f"\n❌ Contract violation: {e}")
except ValueError:
    print("\n❌ Invalid input. Please enter valid numbers.")
