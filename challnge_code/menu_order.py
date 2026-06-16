def main():
    menu_items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0
    while True:
        #prompt user for the item
        item = input("\nItem: ").title()

        #check if we need to end the program
        if item.lower() == "end":
            break

        #check if item is in the dictionary. Reprompt if not
        if item not in menu_items.keys():
            continue

        #Process the order
        total += menu_items[item]

        print(f"Total: ${total:.2f}")

        
main()
