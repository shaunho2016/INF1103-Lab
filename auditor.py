inventory = 0
failed_entries = 0

while True:
    stock = input("Enter stock quantity (or type 'quit' to stop): ")

    # User ends loop with 'quit'
    if stock.lower() == "quit":
        break

    # Check if integer
    if not stock.isdigit():
        print("Error: Invalid input. Please enter a number.")
        failed_entries += 1
        continue

    stock = int(stock)

    # Reject negative number
    if stock < 0:
        print("Error: Negative stock values are not allowed.")
        failed_entries += 1
        continue

    # Add valid stock to inventory
    inventory += stock

    print("Stock accepted.")
    print("Current inventory:", inventory)

    # Check for overstock (more than 500)
    if inventory > 500:
        print("Overstock: Inventory exceeds 500 units.")
        break

# Final report
print("\n--- Inventory Report ---")
print("Total Units Processed:", inventory)
print("Number of Failed/Rejected Entries:", failed_entries)