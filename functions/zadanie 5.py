def sum(number1,number2):
    return number1 + number2
def minus(number1, number2):
    return number1 - number2
def multiply(number1, number2):
    return number1*number2
def divide(number1, number2):
    return number1 / number2

def calculator(number1,number2, operation):
    if operation == "/":
        return divide(number1, number2)
    elif operation == "*":
        return multiply(number1, number2)
    elif operation == "-":
        return minus(number1, number2)
    else:
        return sum(number1, number2)
print(calculator(5,6,"-"))
