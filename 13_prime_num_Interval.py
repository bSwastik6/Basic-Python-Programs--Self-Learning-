# Program to find out Prime Numbers in a given interval.

lower = int(input("Enter the Lower Limit : "))
upper = int(input("Enter the Upper Limit : "))

print("List of Prime Numbers within the given interval : ")

for num in range (lower, upper+1):
    if num > 1:
        for i in range (2, num):
            if num % i == 0:
                break
        else:
            print(num)