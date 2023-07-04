from Assignment9_1 import *

op = MathOperations

while True:                                                        
    print("--------MATH FUNCTIONS--------")
    print("1. Square Root ")
    print("2. Factorial ")
    print("3. Sine value ")
    print("4. Cosine value ")
    print("5. Tangent value")
    print("6. Log Base 2 ")
    print("7. EXIT")

    choice = input("Enter your choice (1-8), or '7' to exit: ")

    if choice == '7':
        print("Exiting")
        break

    x = int(input("Enter the value of x: "))
    result = 0

    if choice == '1':
        result = op.sqrt(x)
        print("Square root:", result)

    elif choice == '2':
        result = op.factorial(x)
        print("Factorial:", result)

    elif choice == '3':
        result = op.sin(x)
        print("Sine:", result)

    elif choice == '4':
        result = op.cos(x)
        print("Cosine:", result)

    elif choice == '5':
        result = op.tan(x)
        print("Tangent:", result)

    elif choice == '6': 
        result = op.log2(x)
        print("Log base 2:", result)

    else:
        print("Invalid choice")

 
    
