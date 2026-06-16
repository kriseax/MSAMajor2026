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
        #create an entry in the dictionary for the item and price
    #close the file

main()