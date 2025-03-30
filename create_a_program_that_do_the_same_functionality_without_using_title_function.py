#Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.

#ask user input a string and use a split method
words = str(input("Enter a string: ")).split()

#create a new list
capitalize_words = []

#loop to the string
for word in words:
    
    #if-else statement
    if 97 <= ord(word[0]) <= 122:

        #converts uppercase if lowercase 
        capitalize_word = chr(ord(word[0]) - 32) + word[1:].lower()
    else:
        capitalize_word = word
    
    capitalize_words.append(capitalize_word)

#print the result without using title() function
print(capitalize_words)