def main():
    #open menu.txt: create a file handler to open file in read mode
    data_file = open("menu.txt", "r")
    print(data_file)

    #create an empty dictionary
    menu_items = {}
    #use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        #split the line at the comma
        item_name_and_price = line_of_data.split(",")
        print(item_name_and_price)

        #get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        #create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price
    
    #close the file
    data_file.close()

    #print all entries from the dictionary
    for items, price in menu_items.items():
        print(f"{items}: ${price}")

main()