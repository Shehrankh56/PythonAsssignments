# 12. Write a Python program to reverse a number using
#  a while loop.
#      Sample Input: num = 12345
#      Sample Output: revnum = 54321


num = int(input("Enter a number: "))
rev = 0

while num > 0:
    rem = num % 10
    rev = rev * 10 + rem
    num //= 10

print("Reversed number is:", rev)