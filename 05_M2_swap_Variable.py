# Swapping values stored in two variables

# Method 2 : Without using a third variable

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

x, y = y, x

print("The value of x : ", x)
print("The value of y : ", y)