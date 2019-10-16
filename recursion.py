import sys

sys.setrecursionlimit(8128)
print(sys.getrecursionlimit())
def factorial(n):
    if n == 0 or n == 1:
         return 1
    else: 
        return n*factorial(n-1)

# print(factorial(int(input())))