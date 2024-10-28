'''### Advanced Requirements:
Have the user input their name, hometown, and age instead of hardcoding the values.
Try giving both your first and second name when asked for your name. What happens? How can you handle multiple words in Python?
Test the program by entering a string value for age (e.g., "twenty"). What happens? How can you prevent this issue?
'''

#declaring variables with str and int to prevent improper input type
Uno_Name = str(input("Enter First Name:"))
Dos_Name = str(input("Enter Second Name:"))
Hometown = str(input("Enter Hometown:"))
Age = int(input("Enter Age:")) 

#displaying questions using print statement

print(  "Please Enter First Name:" + Uno_Name + '\n' + 
        "Please Enter Second Name:" + Dos_Name + '\n' +
        "Please Enter Age:" + str(Age) + '\n' + 
        "Please Enter Hometown:" + Hometown + '\n')