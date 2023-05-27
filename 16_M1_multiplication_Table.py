# Program to display the multiplication table of a number [from 0 -> 10]

# Method 1 : Using for loop.

n = int(input("Enter a number : "))

for i in range(1,11):
    print(n, "x", i, "=", (n*i))