#Prog02. removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.

#ask user input a word
word = input("Enter a word: ")

#ask user input a characters they want to remove
characters = input("Enter a character you want to remove: ")

#if statement
if word[:len(characters)] == characters: 
    removed_prefix = word[len(characters):]

else:
    removed_prefix = word


#prints the word without the removed 
