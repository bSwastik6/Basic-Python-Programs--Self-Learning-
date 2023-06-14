# Program to calculate the N-Powers of an inputted number. 

num = int(input("Enter the number : "))
term = int(input("Enter the number of terms : "))

result = list(map(lambda x : num ** x, range(term+1)))

print(result)

for i in range (term+1):
    print("2 raised to the power",i,":",result[i])