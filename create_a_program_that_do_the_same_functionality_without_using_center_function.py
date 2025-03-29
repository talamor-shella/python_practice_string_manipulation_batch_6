#Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.

#ask user input a string
string = str(input("input a string: "))

#ask user input a number for the width of characters
total_width = int(input("Enter a number for total width: "))

#variable that finds the total spaces need
total_spaces = total_width - len(string)

#split the spaces
left_spaces = total_spaces // 2
right_spaces = total_spaces - left_spaces

#variable that centers the string
center = " " * left_spaces + string + " " * right_spaces

#print the result
