#  4. Write a Python program to find the sum of all odd
#  numbers between two given numbers. 
#      Start = 1, stop = 10
#      Sum of odd numbers: 25


start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
total = 0

for i in range(start, stop + 1):
    if i % 2 != 0:
        total += i

print("Sum of odd numbers:", total)