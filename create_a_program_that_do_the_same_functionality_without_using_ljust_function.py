#Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.

#ask user input a word
word = str(input("Enter a word: "))

#ask user the total length they want
total_length = int(input("Enter a number for the total length: "))

#to find out how many spaces needed
total_spaces = total_length - len(word)

#if-else statement
if total_spaces > 0:
    l_strip = word + " " * total_spaces
else:
    l_strip = word 

#print the word with spaces added
print(f"'{l_strip}'")