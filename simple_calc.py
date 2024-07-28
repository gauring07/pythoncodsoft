print("-----SIMPLE CALCULATOR-----")

def calc():
    def add(a,b):
        return a+b
    def subtract(a,b):
        return a-b
    def multiply(a,b):
        return a*b
    def divide(a,b):
        if b!=0:
            return a/b
        else:
            return "Error (division by 0)"
        
    print("\npress '+' to add \npress '-' to subtract \npress '*' to multiply \npress '/' to divide\n")
    choice=str(input("enter your choice(+,-,*,/):"))

    num1=int(input("\nEnter the first number:"))
    num2=int(input("Enter the second number:"))

    if choice=='+':
        print(f"{num1}+{num2}={add(num1,num2)}")
    elif choice=='-':
        print(f"{num1}-{num2}={subtract(num1,num2)}")
    elif choice=='*':
        print(f"{num1}*{num2}={multiply(num1,num2)}")
    elif choice=='/':
        result=divide(num1,num2)
        if result == "Error (division by 0)":
            print(result)
        else:
            print(f"{num1}/{num2}={divide(num1,num2)}")
    else:
        print("Invalid choice. Try again")
    
    calc()
calc()