# Program to display the multiplication table of a number [from 0 -> 10]

# Method 2 : Using while loop.

n = int(input("Enter a number : "))
i = 1

while i <= 10:
    print(n, "x", i, "=", (n*i))
    i+=1