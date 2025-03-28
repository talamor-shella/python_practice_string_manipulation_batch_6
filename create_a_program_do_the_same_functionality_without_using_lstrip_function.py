#Prog01. lstrip() remove the space characters at the beginning of the string. Create a program that do the same functionality without using lstrip() function.

#ask user input 
word = input("Enter a word: ")

#initialize a variable to zero
spaces = 0

#while loop 
while spaces < len(word) and word(spaces) == " ":

    #increment spaces by 1
    spaces += 1

#prints the remove space characters