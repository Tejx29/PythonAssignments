def add(x,y):                                                 
    return x + y

def sub(x,y):
    return x - y

def mul(x,y):
    return x * y

def div(x,y):
    if y != 0:
        return x / y
    else:
        print("Invalid")
    
def floordiv(x,y):
    return x // y

def expon(x,y):
    return x ** y

def mod(x,y):
    return x % y

while True:                                                         # Main Calculator loop from here
    print("--------CALCULATOR--------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Exponent")
    print("7. Modulus")
    print("8. EXIT")

    choice = input("Enter your choice (1-8): ")

    if choice == '8':
        print("Exiting")
        break

    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))
    result = 0


    if choice == '1':
        result = add(x,y)
     
    elif choice == '2':
        result = sub(x,y)
    
    elif choice == '3':
        result = mul(x,y)

    elif choice == '4':
        result = div(x,y)

    elif choice == '5':
        result = floordiv(x,y)

    elif choice == '6':
        result = expon(x,y)

    elif choice == '7':
        result = mod(x,y)

    else:
        print("Invalid choice")
  
    if choice == '8':
        print("Exiting")
        break

    print("The result is ",result)