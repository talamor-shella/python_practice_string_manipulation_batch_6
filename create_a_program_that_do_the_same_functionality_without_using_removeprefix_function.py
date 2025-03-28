#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#ask user input a word
word = input("Enter a word: ")

#ask user input a characters they want to remove
characters = input("Enter a character you want to remove: ")

remove = 0
#if statement
while remove < len(word):
    if characters in word:
        remove += 1

remove_prefix = word[characters:]    

#prints the word without the removed 
print(remove_prefix)