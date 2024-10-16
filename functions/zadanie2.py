import random

n = int(input())
A = [random.randint(1,1000) for i in range(n)]
even = 0
odd = 0
def is_odd(num):
    return num % 2 != 0

for i in A:
        if is_odd(i) is True:
            odd +=1
        else:
            even +=1

print(A)
print("odd:",odd,"even:",even)
