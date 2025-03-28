#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

#ask user input
word = input("Enter a word: ")

#assume characters aer uppercase
is_upper = True

#use for loop 
for char in word:

    # if-else statement 
    if 97 <= ord(char) <= 122:
        is_upper = False

#prints True if all are uppercase and False if not
print(is_upper)


