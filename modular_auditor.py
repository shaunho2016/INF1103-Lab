inventory = 0
failed_entries = 0

def get_valid_input():
    stock = input("Enter stock quantity (or type 'quit' to stop): ")
    # Check if quit
    if stock.lower() == "quit":
        return "quit"
    #check if integer
    if stock.isdigit():
        stock = int(stock)
        #check if negative
        if stock > 0:
            return(stock)
        else:
            print("Error: Negative stock values are not allowed.")
    else:
        print("Error: Invalid input. Please enter a number.")
        
def process_delivery(current_total,new_value):
    new_total = current_total + new_value
    return(new_total)

def calculate_tax(amount):
    tax = amount * 0.1
    return(tax)

def generate_report(total_units,failed_attempts):
    print("\n--- Inventory Report ---")
    print("Total Units Processed:", total_units)
    print("Number of Failed/Rejected Entries:", failed_attempts)

