# Program to calculate the sum till N Natural Numbers.

num = int(input("Enter a number : "))

if num < 0:
    print("Positive numbers allowed only")
else:
    sum = 0
    while num > 0:
        sum += num
        num -= 1
    print(sum)