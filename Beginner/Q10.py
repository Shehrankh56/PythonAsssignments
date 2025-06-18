# 10. Write a Python program to reverse the order of
#  words in a given sentence.
#   Input_sentence = “Hello, World! Welcome to Python
#  programming.”
#      Output after reverse = “programming. Python to Welcome
#  World! Hell0,

sentence = input("Enter a sentence: ")

words = sentence.split()

reversed_words = words[::-1]

reversed_sentence = ' '.join(reversed_words)

print("Reversed Sentence:", reversed_sentence)