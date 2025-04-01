#Prog08. count() return how many time the function parameter appear in the string. Create a program that do the same functionality without using count() function.

#ask user input word or sentence
string = input("Enter any word or sentence: ").lower()

#ask user input a character they want to count
character = input("Enter a letter or word you want to count: ").lower()

#initialize a counter
count = 0

#for loop
for i in range(len(string) - len(character) + 1):

    #if-else statement   
    if string [i:i+len(character)] == character:
        count += 1

    else:
        count == 0

print(count)