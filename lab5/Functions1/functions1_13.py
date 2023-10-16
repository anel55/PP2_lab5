import random
def guess():
    guess_number = random.randint(1, 20)
    tries_count = 0
    num = 0
    name = input("Hello! What is your name?\n")
    
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    
    
    while(num != guess_number):
        num = int(input("Take a guess\n"))
        tries_count += 1
        if(num < guess_number):
            print("\nYour guess is too low.")
        elif(num > guess_number):
            print("\nYour guess is too big.")

    print(f"Good job, {name}! You guessed my number in {tries_count} guesses!")

guess()