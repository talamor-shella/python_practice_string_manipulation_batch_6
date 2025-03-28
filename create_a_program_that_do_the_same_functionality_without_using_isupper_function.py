#Prog04. isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.

#ask user input
word = input("Enter a word: ")

#use for loop 
for char in word:

    # if-else statement 
    if 65 <= ord(char) <= 90:
        isupper = True

    else:
        isupper = False
print(isupper)


