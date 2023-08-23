def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

def calculator():
    a = float(input("Enter the first number: \n"))  
    print("""
    +
    -
    *
    /      
    """)
    operation = input("Which of the above operations do you want to perform:\n")
    end = False
    while end == False:  
    
        b = float(input("Enter the next number: \n"))

        calc = {"+": add, "-": sub, "*":mul, "/":div}

        cal_func = calc[operation]
        ans = cal_func(a,b)
        print(f'{a} {operation} {b} is {ans}')
        
        choice = input(f"Print do you want to continue with {ans}? yes or no: \n")
        if choice == "yes":
            a = ans
        elif choice == "no":
            again =input("Do you want to continue with new number? yes or no:\n")
            if again == "yes":
                calculator()
            else:
                end = True
                print("Goodbye")

calculator()

        