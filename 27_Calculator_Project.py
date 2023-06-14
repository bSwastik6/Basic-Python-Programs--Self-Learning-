# Mini Calculator Project

print("~~~~~MINI CALCULATOR~~~~~")

num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

print("Press 1 for Addition")
print("Press 2 for Substraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

choice = int(input("Enter your choice based on the above options : "))

if choice == 1:
    print("Result : ", num1 + num2)
elif choice == 2:
    print("Result : ", num1 - num2)
elif choice == 3:
    print("Result : ", num1 * num2)
elif choice == 4:
    print("Result : ", num1 / num2)
else:
    print("Invalid Input")