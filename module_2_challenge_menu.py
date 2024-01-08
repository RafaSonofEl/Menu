
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = []

print("Welcome to the variety food truck.")

place_order = True
while place_order:
    print("From which menu would you like to order? ")
    i = 1
    menu_items = {}
    for key in menu.keys():
        print(f"{i}: {key}")
        menu_items[i] = key
        i += 1

    menu_category = input("Type menu number: ")

    if menu_category.isdigit():
        if int(menu_category) in menu_items.keys():
            menu_category_name = menu_items[int(menu_category)]
            print(f"You selected {menu_category_name}")

            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                            }
                        i += 1

                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item number
            menu_choice = input("Which menu item number would you like to select? ")


            # 3. Check if the customer typed a number
            if menu_choice.isdigit():

                # Convert the menu selection to an integer
                menu_choice = int(menu_choice)


                # 4. Check if the menu selection is in the menu items
                if menu_choice in menu_items.keys():

                    # Store the item name as a variable
                    chosen_menu_item = menu_items[menu_choice]["Item name"]

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {chosen_menu_item} would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                    if quantity.isdigit():
                        quantity = int(quantity)
                    
                    else:
                        quantity = 1

                    # Add the item name, price, and quantity to the order list
                    order_list.append({
                            "Item name": chosen_menu_item,
                            "Price": menu_items[menu_choice]["Price"],
                            "Quantity": quantity
                            })

        else:
            print(f"{menu_category} was not a menu option.")

    else:
        print("You didn't select a number.")
    
    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

               # 5. Check the customer's input
        if keep_ordering.upper() == "Y":
                # Keep ordering
                break
                # Exit the keep ordering question loop
        elif keep_ordering.upper() == "N":
            place_order = False
            break
                # Complete the order

                # Since the customer decided to stop ordering, thank them for
                # their order
            print("Thank you very much for your order!")
                # Exit the keep ordering question loop


                # Tell the customer to try again
        else:
            print("Unfortunately, that item isn't on our menu. Please try again.")


print("This is what we are preparing for you.\n")

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")


# 6. Loop through the items in the customer's order
for customer_chosen_item in order_list:

    # 7. Store the dictionary items as variables
    item_name = customer_chosen_item['Item name']
    price = customer_chosen_item["Price"]
    quantity = customer_chosen_item["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)

    # 9. Create space strings
    item_spaces = " " * num_item_spaces

    # 10. Print the item name, price, and quantity
    print(f"Item name: {item_name}")
    print(f"Price: ${price:.2f}")
    print(f"Quantity: {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

line_costs = (item["Price"] * item["Quantity"] for item in order_list)
final_tally = sum(line_costs)
print(f"The total cost of your order is: ${final_tally:.2f}")