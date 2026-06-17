#Function to add 3 numbers
#Input: number1, number2, number3, All integers
#Output: total:int
def add_numbers(number_1:int, number_2:int, number_3:int) -> int:
    total = number_1 + number_2 + number_3
    c = 18
    return total

def main():
    a = 5
    b = 4
    c = 3

    #Call the add_numbers function and assign the retrned value to answer
    answer = add_numbers(a, b, c)
    print(f"{a} + {b} + {c} = {answer}")
    print(f"{a} + {b} + {c} = {add_numbers(a, b, c)}")
    print(f"c = {c}")

main()