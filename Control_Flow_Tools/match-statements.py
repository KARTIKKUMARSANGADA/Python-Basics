marks=int(input("Enter your marks: "))

def result(marks):
    
    match marks:
        case 90 | 100:
            return "A+"
        case 80 | 89:
            return "A"
        case 70 | 79:
            return "B"
        case 60 | 69:
            return "C"
        case 50 | 59:
            return "D"
        case _ if marks < 50 and marks >= 0:
            return "Fail"
        case _:
            return "Invalid marks"
    