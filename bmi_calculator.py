height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight/(height**2))
print(f"Your BMI is {round(bmi)}")

if bmi <= 18.5 :
    print("You are underweight.")
elif bmi <= 25:
    print("You have a normal weight.")
elif bmi <= 30 :
    print("You are slightly overweight.")
elif bmi <= 35 :
    print("You are obese.")
else:
    print("You are clinically obese.")