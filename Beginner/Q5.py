# 5. Write a Python program to find the factorial of a
#  number using a for loop

num = int(input("Enter a number: "))
fact = 1

for i in range(1, num + 1):
    fact =fact* i

print("Factorial is:", fact)