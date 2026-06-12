def main():
    my_name = "kristofferson"

    #capitalize a string
    print(f"My name capitalized: {my_name.capitalize()}")

    # make a string uppercase
    print(f"My name uppercased: {my_name.upper()}")

    #makea string lowercase
    last_name = "CULMER"
    print(f"My full name lowercased: {my_name.lower()} {last_name.lower()}")

    #compare two strings
    my_name_title_case = "Kristofferson"
    if my_name.lower() == my_name_title_case.lower():
        print("The strings are equal.")
    else:
        print("The strings are not equal")

    print("\nUsing the Startswith() Method\n---------------")
    #determine if a string starts with a set of characters
    print(f"{my_name} starts with a K or k: {my_name.startswith("K") or my_name.startswith("k")}")

    if((not my_name.startswith("Kris")) and (not my_name.startswith("kris"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")

    if((not my_name.lower().startswith("kris"))):
        print(f"You spelled {my_name} incorrectly")
    else:
        print(f"You spelled {my_name} correctly")
    
    print("\nUsing the Endswith() Method\n---------------")
    print(f"{my_name} ends with 'son': {my_name.endswith('son')}")

    print("\nUsing the Find() Method\n---------------")
    
    #Find the f in Kristofferson
    search_letter = "ers"
    index_of_substring = my_name.find(search_letter)
    if index_of_substring != -1:
        print(f"The '{search_letter}' is at index {index_of_substring} in {my_name}")
    else:
        print(f"The is no '{search_letter}' in {my_name}")

    print("\nLooping through a string\n----------")
    for letter in my_name:
        print(letter)

    print(f"{my_name} has {len(my_name)} letters")
    #print the letters in a string along with the index positions
    for letter_index in range(len(my_name)):
        print(f"Letter {letter_index + 1}: {my_name[letter_index]}")

    print("\nSearch a string\n-----------")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    #Write code that counts the number of occurences of the word dog inthe sentence
    #Expected output: 3
    search_word = "dog"
    start_index = 0
    number_of_dogs = 0
    while True:
        #start at the beginning of the string
        #search for the ocurence of the word "dog" starting at index 0
        dog_index = sentence.find(search_word, start_index)

        #search until we dont find anymore dogs: when find() returns -1
        if dog_index == -1:
            break
        else:
            #number_of_dogs = number_of_dogs + 1
            #if we find dog, add 1 to some variable we use to keep track of the 
            number_of_dogs += 1

            #update the starting index by 1
            #continue searching the string from the next index after the dog we just found
            start_index = dog_index + 1
    print(f"There are {number_of_dogs} {search_word}(s) in the sentence.")
        



    

main()