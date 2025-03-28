#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

#ask user input 
word = input("Enter a word: ")

#for loop through each character
for char in word:
    
    #if statement to check if uppercase
    if 65 <= ord(word) <= 90:

        #converts to lowercase if uppercase
        lowercase_letter = chr(ord(word) + 32)

    else:
        lowercase_letter = word #keep if the same

#prints the user input in lower case
print(word)