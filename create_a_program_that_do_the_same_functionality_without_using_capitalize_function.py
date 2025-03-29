#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#ask user input a string
string = str(input("Enter a string: "))

#assign the first index
first_letter = string[0]

#for loop 
for char in string:

    #if-else statement
    if 'a' <= first_letter <= 'z':
        swapcase_letter = chr(ord(char) - 32) #converts lower case to uppercase
    else:
        swapcase_letter = char
    

#print the string without using capitalize function


