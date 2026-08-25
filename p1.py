class ShoppingListManager:
    def __init__(self, budget):
        self.budget = float(budget)
        self.items = []
        self.history = []

    def add_item(self, name, price, quantity, category="General"):
        total_cost = price * quantity
        if total_cost > self.budget:
            self.history.append(f"Failed to add {name}: Exceeds remaining budget.")
            return False
        
        for item in self.items:
            if item["name"].lower() == name.lower():
                item["quantity"] += quantity
                item["price"] = price
                self.budget -= total_cost
                self.history.append(f"Updated {name} quantity and price.")
                return True

        self.items.append({
            "name": name,
            "price": float(price),
            "quantity": int(quantity),
            "category": category
        })
        self.budget -= total_cost
        self.history.append(f"Added {name} to the list.")
        return True

    def remove_item(self, name):
        for index, item in enumerate(self.items):
            if item["name"].lower() == name.lower():
                refund = item["price"] * item["quantity"]
                self.budget += refund
                removed = self.items.pop(index)
                self.history.append(f"Removed {removed['name']} and refunded {refund}.")
                return True
        return False

    def generate_summary(self):
        total_items = sum(item["quantity"] for item in self.items)
        total_spent = sum(item["price"] * item["quantity"] for item in self.items)
        
        print("=== Shopping Summary ===")
        print(f"Total Unique Items: {len(self.items)}")
        print(f"Total Item Count: {total_items}")
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Remaining Budget: ${self.budget:.2f}")
        print("\nDetailed List:")
        for item in self.items:
            cost = item["price"] * item["quantity"]
            print(f"- {item['quantity']}x {item['name']} ({item['category']}) @ ${item['price']:.2f} each = ${cost:.2f}")

# Pre-defined automated execution (No user input)
manager = ShoppingListManager(budget=150.00)

# Operations run automatically
manager.add_item("Apples", 2.50, 4, "Produce")
manager.add_item("Milk", 3.20, 2, "Dairy")
manager.add_item("Steak", 25.00, 3, "Meat")
manager.add_item("Apples", 2.50, 2, "Produce") # Updates existing item quantity
manager.remove_item("Milk")
manager.add_item("Bread", 4.00, 1, "Bakery")

# Display final results
manager.generate_summary()

