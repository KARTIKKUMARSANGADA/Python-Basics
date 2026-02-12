
while True:
        
    num1 = int(input("Enter first number: "))

    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice(1/2/3/4): ")

    if choice not in range(1,5):
        print("Invalid choice")
        exit()

    num2 = int(input("Enter second number: "))

    def add(num1, num2):
        return num1+num2

    def subtract(num1, num2):
        return num1-num2

    def multiply(num1, num2):
        return num1*num2

    def divide(num1, num2):
        if num2 == 0:
            return "Error! Division by zero."
        return num1/num2



    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")   
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

    next_calculation = input("Do you want to perform another calculation? (y/n): ")
    if next_calculation.lower() != 'y':
        break   






