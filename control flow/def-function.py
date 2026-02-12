
n = int(input("Enter a number: "))

def even(n):
    if n % 2 == 0:
        return True
    else:
        return False

def odd(n):
    if n % 2 != 0:
        return True
    else:
        return False
    
if even(n):
    print(f"{n} is an even number.")   
elif odd(n):
    print(f"{n} is an odd number.")
else:
    print("Invalid input.")


