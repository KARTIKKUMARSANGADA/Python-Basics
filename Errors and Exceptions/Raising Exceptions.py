# The raise statement allows the programmer to force a specified exception to occur
# we can add manually any point of code 
 
try:
    age = int(input("Enter your age: "))
    if age < 5:
        raise ValueError("Age cannot be less than 5")
    print(f"You entered: {age}")
except ValueError :
    print("Invalid input. Please enter a valid age.")

# here we are generating a ValueError exception manually using the raise statement if the age entered by the user is less than 5. The except block catches this exception and prints an error message to the user.


