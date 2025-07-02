# Shopping Cart Program

shopping_cart = []
total_cost = 0.0

print("🛒 Welcome to the Shopping Cart Program!")
print("Type 'done' when you are finished.\n")

while True:
    product = input("Enter product name (or type 'done' to finish): ")

    if product.lower() == 'done':
        break

    try:
        price = float(input(f"Enter the price of '{product}': R"))
    except ValueError:
        print("Invalid price. Please enter a number.\n")
        continue

    shopping_cart.append((product, price))
    total_cost += price
    print(f"Added '{product}' for R{price:.2f}\n")

# Summary
print("\n🧾 Your Shopping Cart:")
print("-" * 30)
for item, price in shopping_cart:
    print(f"{item}: R{price:.2f}")
print("-" * 30)
print(f"Total Cost: R{total_cost:.2f}")
