#Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

#ask user input a string
string = input("Enter a string: ")

#ask user input what they want to find the index
character = input("Enter a character you want to find the index: ")

#for loop through string from the last index
for i in range(len(string) - len(character), -1, -1):

    #if statement
    if string[i:i+len(character)] == character:

        #prints the index 
        print(i)
        break