# 9. Write a Python program to count the frequency of
#  each element in a list.
#      Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
#      Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}


lst = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq = {}

for item in lst:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1

print("Frequency count:", freq)