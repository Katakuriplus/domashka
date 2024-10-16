
def multiple(*numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
print(multiple(1,2,3,4,5))