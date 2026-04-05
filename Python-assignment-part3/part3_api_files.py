

with open("python_notes.txt", "w", encoding="utf-8") as f:
    f.write("Topic 1: Variables store data. Python is dynamically typed.\n")
    f.write("Topic 2: Lists are ordered and mutable.\n")
    f.write("Topic 3: Dictionaries store key-value pairs.\n")
    f.write("Topic 4: Loops automate repetitive tasks.\n")
    f.write("Topic 5: Exception handling prevents crashes.\n")

print("File written successfully.")

with open("python_notes.txt", "a", encoding="utf-8") as f:
    f.write("Topic 6: Functions help reuse code.\n")
    f.write("Topic 7: APIs allow communication between systems.\n")

print("Lines appended.")

with open("python_notes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("\nReading file:")

for i, line in enumerate(lines, start=1):
    print(f"{i}. {line.strip()}")

print("Total lines:", len(lines))


# =========================
# API HANDLING
# =========================

import requests

url = "https://dummyjson.com/products?limit=20"

response = requests.get(url)
data = response.json()

products = data["products"]

print("\nID | Title | Category | Price | Rating")
print("-------------------------------------------")

for p in products:
    print(f"{p['id']} | {p['title'][:20]:<20} | {p['category']:<10} | ${p['price']} | {p['rating']}")


# High rated products
filtered = []

for p in products:
    if p["rating"] >= 4.5:
        filtered.append(p)

filtered.sort(key=lambda x: x["price"], reverse=True)

print("\nHigh-rated products:")

for p in filtered:
    print(p["title"], "-", p["price"], "-", p["rating"])


# Category API
url = "https://dummyjson.com/products/category/laptops"

response = requests.get(url)
data = response.json()

print("\nLaptops:")

for p in data["products"]:
    print(p["title"], "-", p["price"])


# POST API
url = "https://dummyjson.com/products/add"

payload = {
    "title": "My Custom Product",
    "price": 999,
    "category": "electronics",
    "description": "A product I created via API"
}

response = requests.post(url, json=payload)

print("\nPOST Response:")
print(response.json())


# =========================
# EXCEPTION HANDLING
# =========================

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"
    except TypeError:
        return "Error: Invalid input types"


print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide("ten", 2))


def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    finally:
        print("File operation attempt complete.")


print(read_file_safe("python_notes.txt"))
print(read_file_safe("ghost_file.txt"))


# =========================
# USER INPUT API
# =========================

while True:
    user_input = input("Enter product ID (1–100) or 'quit': ")

    if user_input.lower() == "quit":
        break

    if not user_input.isdigit():
        print("Invalid input.")
        continue

    pid = int(user_input)

    if pid < 1 or pid > 100:
        print("Out of range.")
        continue

    try:
        res = requests.get(f"https://dummyjson.com/products/{pid}")

        if res.status_code == 404:
            print("Product not found.")
        else:
            data = res.json()
            print(data["title"], "-", data["price"])

    except Exception as e:
        print("Error:", e)


# =========================
# ERROR LOGGING
# =========================

from datetime import datetime

def log_error(function_name, error_type, message):
    with open("error_log.txt", "a") as f:
        time = datetime.now()
        f.write(f"[{time}] ERROR in {function_name}: {error_type} — {message}\n")


# API Error
try:
    requests.get("https://this-host-does-not-exist-xyz.com/api", timeout=5)
except Exception as e:
    log_error("fetch_products", type(e).__name__, str(e))


# HTTP Error
res = requests.get("https://dummyjson.com/products/999")

if res.status_code != 200:
    log_error("lookup_product", "HTTPError", "404 Not Found for product ID 999")


# File Error
try:
    with open("ghost.txt", "r") as f:
        f.read()
except Exception as e:
    log_error("read_file", type(e).__name__, str(e))


# Print Error Log
print("\nError Log:")

with open("error_log.txt", "r") as f:
    print(f.read())