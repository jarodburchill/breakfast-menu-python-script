menu = {
    "small breakfast",
    "regular breakfast",
    "big breakfast",
    "egg",
    "bacon",
    "sausage",
    "hash brown",
    "toast",
    "coffee",
    "tea"
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


while user_input is not "q":
    user_input = input("Enter item (q to terminate): small breakfast, regular breakfast, big breakfast, egg, bacon, sausage, hash brown, toast, coffee, tea: ")
    if user_input != "q":
        add_item()
    print(items)
