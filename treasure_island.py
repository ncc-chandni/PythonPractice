print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first = input("Your are at the cross road. Where do you want to go? Left or Right\n").lower()
if first == "left":
   second = input('You have come to a lake. There is an island in the middle of the lake. Type "wait" to wait for the boat or "swim" to swim across\n').lower()
   if second == "wait":
       third = input("You have arrived at the island unharmed. There is a house with three doors. Red, Yellow or Blue. Which color do you choose?\n").lower()
       if third == "yellow":
           print("You found the treasure. You win")
       elif third == "red":
            print("It's a room full of fire. Game over")
       elif third == "blue":
            print("You enter a room full of beasts. Game over")
       else:
           print("You entered door that doesn't exist. Game over")
   elif second == "swim":
       print("You got attacked by shark. Game over")
   else:
       print("Invalid entry. Game over")
else:
    print("You fell into a hole. Game Over")