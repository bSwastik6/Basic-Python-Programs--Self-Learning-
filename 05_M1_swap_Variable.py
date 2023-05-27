# Swapping values stored in two variables

# Method 1 : Using a third variable

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

temp = x
print("The value of the temporary variable : ", temp)

x = y
print("The value of x : ", x)

y =temp
print("The value of y : ", y)