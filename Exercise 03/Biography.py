'''In this exercise, you'll create a program that stores and prints your name, hometown, and age to the console using a Python dictionary.

### Steps:
1. Store the information (name, hometown, and age) as key-value pairs in a dictionary.
2. Print the values on separate lines using a single `print()` statement.
3. Use variables with appropriate data types for each piece of information.

### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
'''
#declaring variables
Uno_Name = str(input("Enter First Name:"))
Dos_Name = str(input("Enter Second Name:"))
Hometown = str(input("Enter Hometown:"))
Age = int(input("Enter Age:")) 

#displaying questions using print statement

print(  "Please Enter First Name:" + Uno_Name + '\n' + 
        "Please Enter Second Name:" + Dos_Name + '\n' +
        "Please Enter Age:" + str(Age) + '\n' + 
        "Please Enter Hometown:" + Hometown + '\n')