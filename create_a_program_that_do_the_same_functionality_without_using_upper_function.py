#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#ask user input 
string = input("Enter a word: ")

#for loop through string
for char in string:

    #if-else statement for ascii values
    if 97 <= (ord(char)) <= 122:
        
        #convert to upper if lower
        upper_case = chr(ord(char) - 32)

    else:
        upper_case = char    


#prints all characters upper case