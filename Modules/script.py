def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def main():
    print("Testing calculator...")
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(6, 7))
    print(divide(15, 3))


if __name__ == "__main__":
    print("Running script as a standalone program")
    main()
