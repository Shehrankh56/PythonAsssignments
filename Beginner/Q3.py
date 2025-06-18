# 3. Write a Python program to input marks for five
#  subjects Physics, Chemistry, Biology, Mathematics,
#  and Computer. Calculate the percentage and grade
#  according to the following:
#  Percentage >= 90% : Grade A
#  Percentage >= 80% : Grade B
#  Percentage >= 70% : Grade C
#  Percentage >= 60% : Grade D
#  Percentage >= 40% : Grade E
#  Percentage < 40% : Grade F

physics = int(input("Physics marks: "))
chemistry = int(input("Chemistry marks: "))
biology = int(input("Biology marks: "))
maths = int(input("Mathematics marks: "))
computer = int(input("Computer marks: "))

total = physics + chemistry + biology + maths + computer
percentage = total / 5

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 40:
    grade = 'E'
else:
    grade = 'F'

print("Percentage:", percentage)
print("Grade:", grade)