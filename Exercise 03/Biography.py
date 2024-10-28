'''In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

'''
#declaring variables
Name = str(input("Enter First Name:"))
Hometown = str(input("Enter Hometown:"))
Age = int(input("Enter Age:")) 

#displaying questions using print statement

print(  "Please Enter First Name:" + Name + '\n' + 
        "Please Enter Age:" + str(Age) + '\n' + 
        "Please Enter Hometown:" + Hometown + '\n')