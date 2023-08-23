import random
from word_list import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)
blank = list("_" * len(chosen_word))
print(blank)

end = False
counter = 6
while not end:
    guess = input("Guess a letter: \n").lower()
    
    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            blank[i] = letter
    print(blank)
    
    if "_" not in blank:
        end = True
        print("You win")
    
    if guess not in chosen_word:
        counter -= 1
        print(stages[counter])
        print(f"Not match. Lives left {counter}")
        if counter == 0:
            print("You lose")
            end = True

