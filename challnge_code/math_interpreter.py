
def main():
    while True:
        # Prompt the user for the expression
        expression = input("Input Expression (Z Y Z): ")

        # Use .split() to get the parts of the expression. Split at the space
        expression_list = expression.split(" ")

        #cheak that expression list has 3 items
        if len(expression_list) != 3:
            print("ERROR: Incorrect expression format")
            continue

        # Get values from list
        try:
            #   get X and Y and Z values from the list
            #   and check if X and Z are integers by converting to int()
            x = int(expression_list[0])
            operator = expression_list[1]
            z = int(expression_list[2])
        except:
            print("ERROR: X and Z must be integers")
            continue
        
        #Determine the operation to carry out based on the value of the operator
        #Use if/elif/else block to evaluate the operator and carry out the appropriate operation
        #Output the answer
        valid_operators = ["+", "-", "*", "/"]
        if operator not in valid_operators:
            print("ERROR: Operator must be (+, -, *, /)")
            continue

        #Do the math
        if operator == "+":
            answer = x + z
        elif operator == "-":
            answer = x - z
        elif operator == "*":
            answer = x * z
        else:
            if z == 0:
                print("ERROR: Cannot divide by 0")
                continue
            answer = x / z
        # run the expression and print output formatted t one decimal place

        #Print output
        print(f"{x} {operator} {z} = {answer:.1f}")

        #ask the user if they want to evaluate another expression
        do_again = input("Do you want to evaluate another expression? (Press y to continue): ")

        #rerun the program if the user wants to continue, otherwise end the program
        if do_again.lower() != "y":
            break
        
        
main()