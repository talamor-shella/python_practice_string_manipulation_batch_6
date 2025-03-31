#Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

#ask user input a word or sentence
word = input("Enter a word or a sentence: ").lower()

#ask user input starting with 
prefix = input("Enter a prefix in the word: ").lower()
#if-else statement
if word [:len(prefix)] == prefix:

    #returns true
    is_prefix = True

else:
    
    #returns false
    is_prefix = False

#prints true or false
print(is_prefix)