#  11. Write a Python program to calculate the sum of
#  digits of a given number until the sum becomes a
#  single-digit number.
#      Sample Input: num = 987
#      Sample Output: Sum_of_digits = 24,
#      Again compute the sum of digits so that it can be reduced
#  to
#      on single digit.
#      Final Output: 6

num = int(input("Enter a number: "))

while num >= 10:
    temp = num
    sum_digits = 0
    

    while temp > 0:
        digit = temp % 10
        sum_digits += digit
        temp = temp // 10  
    
    
    num = sum_digits

print("Final single-digit sum is:", num)