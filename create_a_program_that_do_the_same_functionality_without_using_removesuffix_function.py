#Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

#Ask user input
string = input("Enter a word: ")

#Ask user they want to remove
character = input("Enter a suffix you want to remove: ")

#if-else statement
if string[-len(character):] == character:
    removed_suffix = len(string) - len(character)
    slice_string = string[:removed_suffix]

else:
    slice_string = string

#prints the characters without the remove suffix
print("remove suffix:", slice_string)