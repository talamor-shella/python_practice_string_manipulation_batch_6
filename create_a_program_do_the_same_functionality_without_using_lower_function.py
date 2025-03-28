#Prog03. lower() converts all characters of the string into lower case. Create a program that do the same functionality without using lower() function.

#ask user input 
word = str(input("Enter a word: "))

#make a new list
new_word = []

#for loop through each character
for char in word:
    
    #if statement to check if uppercase
    if 65 <= ord(char) <= 90:

        #converts to lowercase if uppercase
        lowercase_letter = chr(ord(char) + 32)

    else:
        lowercase_letter = char #keep if the same

    new_word.append(lowercase_letter)    

#variable the joins the individual elements in the list
join_elements = "".join(new_word)

#prints the user input in lower case
print(f"Characters in lowercase: {join_elements}")