#Prog09. index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.

#ask user input a string
string = input("Enter a word: ").lower()

#ask user input what they want to find the index
character = input("Enter a character you want to find the index: ").lower()
#for loop
for i in range(len(string) - len(character) + 1):

    #if statement 
    if string[i:i+len(character)] == character:

        #prints the index 
        print(i)
        break