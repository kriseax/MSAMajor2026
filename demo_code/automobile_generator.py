from Automobile import Automobile

def main():
    #create instances of automobiles
    auto1 = Automobile("Honda", "Accord", "23456", 2.4, "Alice", 2024, "Blue")
    auto2 = Automobile("Ferrari", "F-50", "12345", 4.8, "Bob", 2022, "Black")

    #change some proprty values
    auto1.year = 2014

    #create a list of automobiles
    auto_list: list[Automobile] = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    #print all automobile data
    for auto in auto_list:
        auto.print_data()

    print(f"Auto1 is {auto1.get_age()} years old")

main()