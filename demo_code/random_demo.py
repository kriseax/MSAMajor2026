import random
def main():
    #create a random number generator
    random_generator = random.Random()
    random_number = random_generator.randint(0, 100)
    print(f"Random value: {random_number}")

    #generate 20 random numbers
    print("\nGenerate 20 Random numbers\n----------")
    for _ in range(20):
        print(random_generator.randint(0, 100))

main()