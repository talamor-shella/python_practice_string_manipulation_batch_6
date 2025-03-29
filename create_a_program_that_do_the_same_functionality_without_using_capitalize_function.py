#Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.

#ask user input a string
string = str(input("Enter a string: "))


#if-else statement
if string: 
    capitalize_string = string[0].upper() + string[1:].lower()
else:
    capitalize_string = ""
#print the string without using capitalize function

print(f"String in capitalize: {capitalize_string}")