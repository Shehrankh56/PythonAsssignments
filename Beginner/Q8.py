#  8. Write a Python program to calculate the LCM (Least
#  Common Multiple) of two numbers.
#      number1 = 12, number2 = 18
#      LCM of 12 and 18 are: 36

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM is:", max_num)
        break
    max_num += 1