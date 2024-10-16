def calculator(number1,number2, operation):
    if operation == "/":
        result = number1/number2
    elif operation == "*":
        result = number1*number2
    elif operation == "-":
        result = number1 - number2
    else:
        result = number2+number1
    return result
print(calculator(5,6,"*"))
