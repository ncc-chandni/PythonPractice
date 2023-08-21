#Calculate the how much each person should pay on splitting the total bill including the tip

bill = float(input("What is your total bill? \n$"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n "))
people = int(input("How many people to split the bill? \n"))

total = float(bill + ((bill * tip)/100))
split_bill = float(total/people)

print(f'Each person should pay: ${round(split_bill,2)}')