#  2. Write a program that accepts a string as input from
#  the user and calculates the number of digits and
#  letters.
#      Input: Hello123 
#      Output: Alphabets: 5 & Number : 

s = input("Enter a string: ")
letters = 0
digits = 0

for ch in s:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1

print("Alphabets:", letters, "& Number:", digits)