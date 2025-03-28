#Prog05. endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.

#ask user input
word = input("Enter a word: ")

#ask user input the suffix
suffix = input("Enter a suffix: ")

#if statement 
if word [-len(suffix):] == suffix:
    
    #returns true 
    endswith = True

else:

    #returns False
    endswith = False

print(endswith)