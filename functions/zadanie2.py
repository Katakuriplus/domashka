import random


def is_odd(num):
    return num % 2 != 0
def count_even_odd(n):
    A = [random.randint(1, 1000) for _ in range(n)]
    even = 0
    odd = 0
    for i in A:
        if is_odd(i):
            odd += 1
        else:
            even += 1
    return {'odd': odd,'even': even}


n = int(input())
result = count_even_odd(n)
print(result)

