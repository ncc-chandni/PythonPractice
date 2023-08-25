import random

print("Welcome to number Guessing Game!")

print("I am thinking of a number between 1 to 100")
number = random.randint(1,100)
print(number)

def check_level(level):
    if level == 'easy':
        i = 10
        return i
    else:
        i = 5
        return i


level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = check_level(level)
print(f" Attempts = {attempts}")

def check_number(guess):
    if guess < number:
        print("Too Low")
    elif guess > number:
        print("Too High")
    elif guess == number:
        print("Correct. You win!")


while attempts > 0:
    print(f"You have {attempts} attempts left")
    attempts -= 1
    guess = int(input("Make a guess:  "))
    check_number(guess)
    if guess == number:
        break

if attempts == 0 and guess != number:
    print("You are out of attempts. You lose")


