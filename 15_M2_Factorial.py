# Program to calculate the factorial of a number.

# Method 2 : Using Recursion

def factorial(n):
    if n == 0:
        return 1
    else:
        return ((n) * factorial(n-1))

n = int(input("Input a number : "))

result = factorial(n)
print("The Factorial of", n, "is :", result)