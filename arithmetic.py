import math

PI = 3.1415

def addition():
    a, b = map(float, input("Enter two numbers you would like to add: ").split())
    print(a + b)

def subtraction():
    a, b = map( float, input("Please enter two numbers you would like to subtract: ").split())
    print(a - b)

def division():
    a, b = map(float, input("Enter the two values you would like to divide: ").split())
    
    if(b == 0):
        print("You cannot divide by zero!")
        return
    print(a / b)  

def multiplication():
    a, b = map(float, input("Enter the two values you would like to multiply: ").split())
    print(a * b)

def square():
    a = float(input("Enter in the value you would like to find the square value of: "))
    print(a * a)

def squareRoot():
    a = float(input("Enter in the value you would like to find the square root of: "))
    result = math.sqrt(a)
    print(result)

def exponent():
    a, b = map(float, input("Enter the base and exponent: ").split())
    result = a ** b
    print(result)

def sin():
    a = float(input("Enter in an angle to find the sine: "))
    result = math.sin(a)
    print(result)

def cos():
    a = float(input("Enter in an angle in degrees to find the cosine: "))
    result = math.cos(a)
    print(result)

def tan():
    a = float(input("Enter in the angle in degrees to find the tangent: "))
    result = math.tan(a)
    print(result)

def main():
    while True:

        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Square")
        print("6. Square Root")
        print("7. Exponent")
        print("8. Sin")
        print("9. Cos")
        print("10. Tan")
        print("11. Quit")
              
        choice = input("Choose an operation (1-11): ")
 

        if choice == "1":
            addition()
        elif choice == "2":
            subtraction()
        elif choice == "3":
            multiplication()
        elif choice == "4":
            division()
        elif choice == "5":
            square()
        elif choice == "6":
            squareRoot()
        elif choice == "7":
            exponent()
        elif choice == "8":
            sin()
        elif choice == "9":
            cos()
        elif choice == "10":
            tan()
        elif choice == "11":
            print("Goodbye!")
            break  # exits the loop
        else:
            print("Invalid choice, try again.")

main()