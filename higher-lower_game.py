from game_data import data
import random

def describe(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f'{name}, {description}, {country}'

def compare(guess, follower_a, follower_b):
    if follower_a > follower_b and guess == 'a':
        return True
    elif follower_a < follower_b and guess == 'b':
        return True

score = 0
game_continue = True
b = random.choice(data)

while game_continue:
    a = b
    b = random.choice(data)
    while a == b:
        b = random.choice(data)
    print(f"Compare A: {describe(a)}")
    print("VS")
    print(f'Against B: {describe(b)}')

    follower_a = a["follower_count"]
    follower_b = b["follower_count"]

    guess = input("Who has more followers? Type 'A' or 'B: ").lower()
    correct = compare(guess, follower_a, follower_b)
    if correct:
        score += 1
        print(f"You are correct. Your current score is {score}")
    else:
        game_continue = False
        print(f"Sorry that's wrong. Final score {score}")
