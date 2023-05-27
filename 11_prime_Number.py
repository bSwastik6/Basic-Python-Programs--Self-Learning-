# Program to determine whether the inputted number is a Prime Number or not.

num = int(input("Enter a number : "))

if num == 1:
    print(num, " is not a Prime Number")
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, " is not a Prime Number")
            break
    else:
        print(num, " is a Prime Number")