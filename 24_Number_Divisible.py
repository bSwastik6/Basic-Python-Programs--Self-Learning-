# Program to find out which numbers are divisible by the inputted number in the range of 1 to 100.

num = int(input("Enter the number to check for divisibility : "))

for i in range(1,100):
    if i % num == 0:
        print(i)