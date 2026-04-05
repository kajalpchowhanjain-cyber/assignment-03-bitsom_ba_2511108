raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

for student in raw_students:
    name = student["name"].strip().title()
    roll = int(student["roll"])
    
    marks = [int(x) for x in student["marks_str"].split(", ")]
    
    valid = all(word.isalpha() for word in name.split())
    status = "✓ Valid name" if valid else "✗ Invalid name"

    print("================================")
    print(f"Student : {name}")
    print(f"Roll No : {roll}")
    print(f"Marks   : {marks}")
    print(status)
    print("================================")


# ---- Task 1 code above ----

# roll 103 check
for student in raw_students:
    if int(student["roll"]) == 103:
        name = student["name"].strip().title()
        print(name.upper())
        print(name.lower())

# ---- Task 2 starts HERE ----

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

for sub, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else:
        grade = "F"
    
    print(f"{sub} : {mark} → {grade}")

    total = sum(marks)
average = round(total / len(marks), 2)

print("Total:", total)
print("Average:", average)

max_marks = max(marks)
min_marks = min(marks)

max_index = marks.index(max_marks)
min_index = marks.index(min_marks)

print("Highest:", subjects[max_index], "-", max_marks)
print("Lowest:", subjects[min_index], "-", min_marks)

new_subjects = 0

while True:
    subject = input("Enter subject name (or type 'done'): ")
    
    if subject.lower() == "done":
        break

    mark_input = input("Enter marks (0–100): ")

    if not mark_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue

    mark = int(mark_input)

    if mark < 0 or mark > 100:
        print("Marks should be between 0 and 100.")
        continue

    subjects.append(subject)
    marks.append(mark)
    new_subjects += 1

    print("New subjects added:", new_subjects)

total = sum(marks)
average = round(total / len(marks), 2)

print("Updated Average:", average)

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\nName              | Average | Status")
print("----------------------------------------")

pass_count = 0
fail_count = 0
total_avg = 0
topper_name = ""
topper_avg = 0

for name, marks in class_data:
    avg = round(sum(marks) / len(marks), 2)
    
    status = "Pass" if avg >= 60 else "Fail"
    
    print(f"{name:<18} | {avg:^7} | {status}")

    total_avg += avg

    if status == "Pass":
        pass_count += 1
    else:
        fail_count += 1

    if avg > topper_avg:
        topper_avg = avg
        topper_name = name

        
print("\nPassed:", pass_count)
print("Failed:", fail_count)
print("Topper:", topper_name, "-", topper_avg)

class_average = round(total_avg / len(class_data), 2)
print("Class Average:", class_average)

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
clean_essay = essay.strip()
print("Stripped:", clean_essay)
print("Title Case:", clean_essay.title())
count = clean_essay.count("python")
print("Count of 'python':", count)
replaced = clean_essay.replace("python", "Python 🐍")
print("Replaced:", replaced)
sentences = clean_essay.split(". ")
print("Sentences:", sentences)
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence += "."
    print(f"{i}. {sentence}")

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