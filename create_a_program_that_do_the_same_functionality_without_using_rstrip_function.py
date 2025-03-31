#Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

#ask user input
string = input("Enter a word: ")

#variable finding the last non-space character
last_index = 0

#for loop
for i in range(len(string) - 1, -1, -1):
    
    #if statement to find non space character
    if string[i] != " ":

        last_index = i
        break

#variable that take out only the trailing spaces
trailing_spaces = string[last_index + 1:]

#use replace() to remove the spaces
rstrip_string = string.replace(trailing_spaces, "")


