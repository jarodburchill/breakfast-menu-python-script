menu = {
    "small breakfast": None,
    "regular breakfast": None,
    "big breakfast": None,
    "egg": 0.99,
    "bacon": 0.49,
    "sausage": 1.49,
    "hash brown": 1.19,
    "toast": 0.79,
    "coffee": 1.09,
    "tea": 0.89
}

items = []

user_input = ""

def add_item():
    global menu
    global items
    global user_input
    if user_input in menu:
        try:
            quantity = int(input("Quantity: "))        
        except ValueError:
            print("Please enter a valid quantity.")
        except Exception as e:
            print("Something went wrong: " + str(e))
        for x in range(quantity):
            items.append(user_input)
    else:
        print("Please enter a valid item.")

def calculate_subtotal():
    global items
    subtotal = 0.00
    for item in items:
        item_total = 0.00
        if item == "small breakfast":
            item_total = calculate_combo(1, 1, 2, 2, 1)
        elif item == "regular breakfast":
            item_total = calculate_combo(2, 1, 2, 4, 2)
        elif item == "big breakfast":
            item_total = calculate_combo(3, 2, 4, 6, 3)
        else:
            item_total = menu[item]
        print(item + ": " + str('${:,.2f}'.format(item_total)))
        subtotal += item_total
    return subtotal

def calculate_combo(eggs, hash_browns, toast, bacon, sausages):
    item_total = 0.00
    item_total += menu["egg"] * eggs
    item_total += menu["hash brown"] * hash_browns
    item_total += menu["toast"] * toast
    item_total += menu["bacon"] * bacon
    item_total += menu["sausage"] * sausages
    return item_total

def format_input(text):
    text = text.lower().strip()
    words = text.split()
    text = " ".join(words)
    return text

while user_input != "q":
    user_input = format_input(input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, " + 
        "egg, bacon, sausage, hash brown, toast, coffee, tea: "))
    if user_input != "q":
        add_item()
    else:
        subtotal = calculate_subtotal()
        tax = subtotal * 0.13
        total = subtotal + tax
        print("Subtotal: " + str('${:,.2f}'.format(subtotal)))
        print("Tax: " + str('${:,.2f}'.format(tax)))
        print("Total: " + str('${:,.2f}'.format(total)))
