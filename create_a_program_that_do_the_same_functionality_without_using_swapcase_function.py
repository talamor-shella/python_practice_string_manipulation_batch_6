#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

#ask user input a string
string = str(input("Enter a string: "))

#looping to the string
for char in string:

    #if-else statement
    if 97 <= ord(char) <= 122:
        swapcase_letter = chr(ord(char) - 32) #lower to upper

    else:
        swapcase_letter = chr(ord(char) + 32) #upper to lower


#prints the string without using swapcase