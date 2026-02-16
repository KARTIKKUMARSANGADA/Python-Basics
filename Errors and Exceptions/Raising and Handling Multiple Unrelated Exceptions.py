try:
    num = int(input("Enter number: "))
    print(10 / num)
except (ValueError, ZeroDivisionError):
    print("Invalid input.")
    
# you can add multiple errors in a single except block by using a tuple. This way, if any of the specified exceptions occur, the same error message will be printed.
# you create separate except block for each type of exception,then that you can create a single except block that handles multiple exceptions by using a tuple of exception types. 


def f():
    raise ExceptionGroup(
        "group1",
        [
            OSError(1),
            SystemError(2),
            ExceptionGroup(
                "group2",
                [
                    OSError(3),
                    RecursionError(4)
                ]
            )
        ]
    )

try:
    f()
except* OSError as e:
    print("There were OSErrors")
except* SystemError as e:
    print("There were SystemErrors")
    
# * is used to catch multiple exceptions of the same type that are raised within an ExceptionGroup. It allows you to handle all exceptions of that type together, even if they are nested within other ExceptionGroups.