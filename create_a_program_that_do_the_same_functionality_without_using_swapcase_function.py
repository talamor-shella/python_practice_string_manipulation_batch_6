#Prog08. swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.

#ask user input a string
string = str(input("Enter a string: "))

#make a new list for swapcaseletter
new_string = []

#looping to the string
for char in string:

    #if-else statement
    if 97 <= ord(char) <= 122:
        swapcase_letter = chr(ord(char) - 32) #lower to upper

    else:
        swapcase_letter = chr(ord(char) + 32) #upper to lower

    new_string.append(swapcase_letter)

#use join function to make it into one string
join_string = "".join(new_string)

#prints the string without using 
