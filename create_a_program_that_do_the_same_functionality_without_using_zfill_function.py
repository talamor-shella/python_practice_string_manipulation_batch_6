#Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using zfill() function

#ask user input a number
number = (input("Enter a number: "))

#ask user specified length
specified_length = int(input("Enter a number for specified length: "))

#find total space needed to add zeros
total_space = specified_length - len(number)

#if statement using rjust function and else statement
if total_space > 0:
    fill_zero = number.rjust(specified_length,"0")

else:
    fill_zero = number

#prints the complete number of characters
