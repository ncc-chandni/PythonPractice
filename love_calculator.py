print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

name_1_2 = name1 + name2
T = name_1_2.count("t")
R = name_1_2.count("r")
U = name_1_2.count("u")
E = name_1_2.count("e")
L = name_1_2.count("l")
O = name_1_2.count("o")
V = name_1_2.count("v")
E = name_1_2.count("e")

TRUE = T + R + U + E
LOVE = L + O + V + E

score = str(TRUE) + str(LOVE)

if int(score) < 10 or int(score) > 90:
    print(f'Your score is {score}, you go together like coke and mentos.' )
elif int(score) >= 40 and int(score) <= 50:
    print(f'Your score is {score}, you are alright together.')
else:
    print(f'Your score is {score}')
