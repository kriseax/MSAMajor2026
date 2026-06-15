def main():
    #create a list of strings, integers, and differing values
    names = ["John", "Mary", "Alice", "Bob"]
    list_of_integers = [10, 16, 24, 42, 14, 9]
    random_type_list = ["Cyd", 15, 22.3, True, "Frank"]
    empty_list = []

    #Print a list
    print(list_of_integers)

    #Add values to a list
    print("\nAddig Values to a List\n----------")
    names.append("Johnny")
    list_of_integers.append(63)
    list_of_integers.append(5)

    print(f"List of Integers: {list_of_integers}")
    print(f"List of names: {names}")

    print("\nGet the number of items in a list\n----------")
    print(f"Items in Integer list: {len(list_of_integers)}")
    print(f"Items in Names list: {len(names)}")
    print(f"Items in Empty list: {len(empty_list)}")

    print("\nGet values at specific indices in a list\n---------")
    print(f"First item in names list: {names[0]}")
    print(f"Fourth item in names list: {names[3]}")

    #Print all items in a list
    print("\nPrinting all names\n-----------")
    for name in names:
        print(name)

    print("\nPrinting all names with index values\n-----------")
    for index in range(len(names)):
        print(f"names[{index}] -> {names[index]}") 

    #Calculate the sum of all values in a list
    sum_of_all_integers = 0
    for number in list_of_integers:
        #sum_of_all_integers = sum_of_all_integers + number
        sum_of_all_integers += number
    
    print(f"Sum of all intgers: {sum_of_all_integers}")

    #Calulate the average of all integers in list
    avg_of_all_integers = sum_of_all_integers / len(list_of_integers)
    print(f"Average of all Integers: {avg_of_all_integers:.2f}")

    #Does the list contain a specific item
    search_name = "Alice"
    if search_name not in names:
        print(f"{search_name} is not in the names list")
    else:
        print(f"{search_name} is in the names list")

    #Find the largest value in a list
    #set max_value to the value of the first item in the list
    max_value = list_of_integers[0]

    #loop over the entire list
    for current_value in list_of_integers:
        #if current_value > max_value, set max_value to current_value
        if current_value < max_value:
            max_value = current_value
    
    #After the loop is done, print the largest value
    print(f"\nList of Inegers: {list_of_integers}")
    print(f"Smallest value in list of integers: {max_value}")





    




main()