import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def black_jack():
    
    def deal_card(i):
        a = random.choices(cards, k = i)
        return a

    computer = deal_card(2)
    user = deal_card(2)
    print(f"Computer's first card: {computer[0]}")
    print(f"You cards: {user}")

    def calc_score(card_list):
        total = sum(card_list)
        if total == 21 and len(card_list) == 2:
           return 0
        if 11 in card_list and sum(card_list) > 21:
            card_list.remove(11)
            card_list.append(1)
            total = sum(card_list )
        return total

    tot_user = calc_score(user)
    tot_comp = calc_score(computer)

    while tot_user < 21:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            a = deal_card(1)
            for i in a:
                user.append(i)
            tot_user = calc_score(user)
            print(f"Your final cards {user}, current score {tot_user}")
        else:
            print(f"Your final cards {user}, current score {tot_user}")
            break

    while tot_comp <= 17:
        b = deal_card(1)
        for i in b:
            computer.append(i)
        tot_comp = calc_score(computer)
    print(f"Computer's final cards {computer}, computer's score {tot_comp}")


    def compare_score(a,b):
        if (a > b and a < 21) or (b > 21):
            print("You win!")
        elif (a < b and b < 21) or (a > 21) :
            print("You lose")
        elif a == b:
            print("It's a draw")
        elif a == 0:
            print("You win with a blackjack")
        elif b == 0:
            print("You Lose. Computer has a blackjack")
    compare_score(tot_user, tot_comp)


black_jack()
choice = input("Do you want to play again? Type 'yes' to play or 'no' to exit.\n")
if choice == "yes":
    black_jack()
else:
    print("Goodbye")