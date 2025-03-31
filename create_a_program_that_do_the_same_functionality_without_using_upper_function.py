#Prog03. upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.

#ask user input 
string = input("Enter a word: ")

#make a new list for uppercased letters
upper_cased_list = []

#for loop through string
for char in string:

    #if-else statement for ascii values
    if 97 <= (ord(char)) <= 122:
        
        #convert to upper if lower
        upper_case = chr(ord(char) - 32)

    else:
        upper_case = char    

    upper_cased_list.append(upper_case)

#prints all characters upper case
print(upper_cased_list) #for checking only