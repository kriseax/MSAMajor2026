#Function to load data fram a file and return a dictioinary
#Input: filename: string
#Output: dictionary
def load_menu_items(filename:str) -> dict:
    #open menu.txt: create a file handler to open file in read mode
    data_file = open(filename, "r")

    #create an empty dictionary
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the line at the comma
        item_name_and_price = line_of_data.split(",")

        #get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    
    #close the file
    data_file.close()

    #return the dictionary of menu items
    return menu_items


def main():
    menu_items = load_menu_items("menu.txt")

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