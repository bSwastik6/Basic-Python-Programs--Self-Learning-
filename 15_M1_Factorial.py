# Program to calculate the factorial of a number.

# Method 1 : Using for loop

num = int(input("Enter a number : "))
fact = 1

if num < 0:
    print("Factorial of negative numbers does not exist.")
if num == 0:
    print("Factorial of 0 : ",1)
if num > 0:
    for i in range(1, num+1):
        fact = fact * i

print("The Factorial of", num, "is :", fact)