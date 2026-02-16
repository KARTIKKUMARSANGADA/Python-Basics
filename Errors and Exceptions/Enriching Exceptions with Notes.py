# Enriching exceptions with notes means adding extra information to an error after it is raised — without changing the original error message.

# # exception.add_note("extra message")
# try:
#     raise ValueError("Invalid number")
# except ValueError as e:
#     e.add_note("The number must be positive.")
    

# you can add multiple notes to an exception.

a=10
b=0

def divide(a, b):
    try:    
        return a / b
    except ZeroDivisionError as e:
        e.add_note("You tried dividing by zero.")
        e.add_note(f"Values were: a={a}, b={b}")
        raise
divide(a, b)