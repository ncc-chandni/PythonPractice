# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
alpha = int(input("How many letters would you like in your password?\n"))
sym = int(input("How many symbols would you like?\n"))
num = int(input("How many numbers would you like?\n"))

pass_alpha = random.choices(letters, k = alpha)
pass_sym = random.choices(symbols, k = sym)
pass_num = random.choices(numbers, k = num)

password = pass_alpha + pass_sym + pass_num
print(f"Easy Level Password : {''.join(password)}")

random.shuffle(password)
print(f"Hard Level Password: {''.join(password)}")
