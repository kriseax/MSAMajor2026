import random
import math

def get_level_choice():
    """
    Function to get level choice from user
    Inputs: none
    Returns: string user choice
    """
    while True:
        user_choice = input("Enter Level 1, 2, 3: ")
        if user_choice not in ["1", "2", "3"]:
            print("Error: Invalid input!\n")
        else:
            return int(user_choice)

def get_number_of_questions():
    while True:
        try:
            num_questions = int(input("\nEnter number of questions to ask (3 to 10): "))
            if num_questions < 3 or num_questions > 10:
                print("ERROR: Please enter an integer value between 3 and 10!")
                continue
            return num_questions
        except ValueError:
            print("ERROR: Please enter an integer value between 3 and 10!")

def main():
    max_tries = 3
    total_correct = 0

    # Get level
    level = get_level_choice()

    # Get number of questions
    number_of_questions = get_number_of_questions()

    # Generate addition problems
    for question in range(number_of_questions):

        if level == 1:
            start_value = 0
            stop_value = 9
        elif level == 2:
            start_value = 10
            stop_value = 99
        else:
            start_value = 100
            stop_value = 999

        # Generate 2 random numbers
        number1 = random.randint(start_value, stop_value)
        number2 = random.randint(start_value, stop_value)
        answer = number1 + number2

        total_tries = 0

        while total_tries < max_tries:
            try:
                user_answer = int(input(f"{number1} + {number2} = "))
            except ValueError:
                total_tries += 1
                print("WRONG!!!\n")
                continue
            
            if user_answer == answer:
                    total_correct += 1
                    print("CORRECT!!!\n")
                    break
            else:
                total_tries += 1
                print("WRONG!!!\n")
                continue

        if total_tries == max_tries:
            print(f"Correct Answer: {number1} + {number2} = {answer}\n")

    score_percentage = (total_correct / number_of_questions) * 100

    # Print score
    print(f"\nYou got {total_correct} out of {number_of_questions} questions correct: {score_percentage:.2f}%")


main()