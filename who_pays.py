#The person selected will have to pay for everybody's food bill.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

selected = random.randrange(len(names))
print(f'{names[selected]} is going to buy the meal today!')