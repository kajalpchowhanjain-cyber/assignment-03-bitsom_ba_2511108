menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}
    
categories = ["Starters", "Mains", "Desserts"]

for cat in categories:
    print(f"\n===== {cat} =====")
    
    for item, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{item:<15} ₹{details['price']:<6} [{status}]")

            # Total items
print("\nTotal items:", len(menu))

# Available items
available_count = 0
for item in menu:
    if menu[item]["available"]:
        available_count += 1

print("Available items:", available_count)

max_price = 0
expensive_item = ""

for item, details in menu.items():
    if details["price"] > max_price:
        max_price = details["price"]
        expensive_item = item

print("Most expensive:", expensive_item, "-", max_price)

print("\nItems under ₹150:")

for item, details in menu.items():
    if details["price"] < 150:
        print(item, "-", details["price"])

    
    
    



# ----------- FUNCTION -----------

def add_to_cart(item_name, qty):
    if item_name not in menu:
        print("Item not found in menu")
        return

    if not menu[item_name]["available"]:
        print("Item is unavailable")
        return

    found = False

    for c in cart:
        if c["item"] == item_name:
            c["quantity"] += qty
            found = True
            break

    if not found:
        cart.append({
            "item": item_name,
            "quantity": qty,
            "price": menu[item_name]["price"]
        })


# ----------- CART OPERATIONS -----------

cart = []

add_to_cart("Paneer Tikka", 2)
add_to_cart("Gulab Jamun", 1)
add_to_cart("Paneer Tikka", 1)
add_to_cart("Mystery Burger", 1)
add_to_cart("Chicken Wings", 1)


# ----------- REMOVE ITEM -----------

remove_item = "Gulab Jamun"

found = False

for c in cart:
    if c["item"] == remove_item:
        cart.remove(c)
        found = True
        break

if not found:
    print("Item not in cart")


# ----------- FINAL OUTPUT -----------

print("\nFinal Cart:", cart)

print("\n========== Order Summary ==========")

subtotal = 0

for item in cart:
    item_total = item["quantity"] * item["price"]
    subtotal += item_total

    print(f"{item['item']:<15} x{item['quantity']}   ₹{item_total}")

    print("----------------------------------")

gst = subtotal * 0.05
total = subtotal + gst

print(f"Subtotal:      ₹{subtotal}")
print(f"GST (5%):      ₹{round(gst, 2)}")
print(f"Total:         ₹{round(total, 2)}")

print("==================================")

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}

print("\nRevenue per day:")

daily_revenue = {}

for date, orders in sales_log.items():
    total = 0
    for order in orders:
        total += order["total"]
    
    daily_revenue[date] = total
    print(date, ":", total)

    best_day = max(daily_revenue, key=daily_revenue.get)

print("Best day:", best_day, "-", daily_revenue[best_day])

item_count = {}

for orders in sales_log.values():
    for order in orders:
        for item in order["items"]:
            if item not in item_count:
                item_count[item] = 0
            item_count[item] += 1

most_ordered = max(item_count, key=item_count.get)

print("Most ordered item:", most_ordered)

sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\nAll Orders:")

count = 1

for date, orders in sales_log.items():
    for order in orders:
        items = ", ".join(order["items"])
        print(f"{count}. [{date}] Order #{order['order_id']} — ₹{order['total']} — Items: {items}")
        count += 1