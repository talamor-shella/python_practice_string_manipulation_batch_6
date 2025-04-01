#Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

#ask user input a word
string = input("Enter a word: ")

#ask user total length 
total_length = int(input("Enter a number for total length: "))

#find how many spaces need
spaces_need = total_length - len(string)

#if-else statement
if spaces_need > 0:
    right_strip =  " " * spaces_need + string
else:
    right_strip = string

#print the word with spaces 
