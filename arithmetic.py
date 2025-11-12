import math

PI = 3.1415

def addition():
    return a + b

def subtraction():
    return a - b

def division():    
    if(b == 0):
        return "Error: Division by zero"
    return a / b

def multiplication():
    return a * b

def remainder():
    if b == 0:
        return "Error: Division by zero"
    return a % b
    
def square():
    a * a

def squareRoot():
    if (a < 0):
        return "The answer is imaginary, but you're not ready for that one."
    return math.sqrt(a)

def exponent():
    return a ** b

def factorials():
    if a < 0 or a != (int)(a):
        return "Factorials are only found for non-negative whole numbers"
    i = 0
    for i in a:
        result = a * i
        i+=1
    return result

def sin():
    return math.sin(math.radians(a))

def cos():
    return math.cos(math.radians(a))

def tan():
    return math.tan(math.radians(a))

def main():
    while True:

        print("\n--- Fancy Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Remainder")
        print("6. Square")
        print("7. Square Root")
        print("8. Exponent")
        print("9. Factorials")
        print("10. Sin")
        print("11. Cos")
        print("12. Tan")
        print("13. Quit")
              
        choice = int(input("Choose an operation (1-13): "))
 

        match(choice):
            case 1:
                addition()
            case 2:
                subtraction()
            case 3:
                multiplication()
            case 4:
                division()
            case 5:
                remainder()
            case 6:
                square()
            case 7:
                squareRoot()
            case 8:
                exponent()
            case 9:
                factorials()
            case 10:
                sin()
            case 11:
                cos()
            case 12:
                tan()
            case 13:
                break
            case _:
                print("Invalid operation.")
                choice = int(input("Select an operation (1-13): "))

main()
