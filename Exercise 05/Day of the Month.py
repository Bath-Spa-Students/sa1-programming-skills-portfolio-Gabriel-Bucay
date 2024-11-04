'''
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Instructions:
1. Create a Dictionary: Define a dictionary where the keys are month numbers and the values are the number of days in those months.
2. Input Handling: Ask the user to input the month number.
3. Check and Output: Use an if-else statement to check if the input is valid and print the number of days in the corresponding month.
'''
#setting dictionary without leap year (Numbers on left = months | Numbers on right = days)
Calendar = {
    1: 31, 
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}
#Asking for user input and setting 1-12 as months
month = int(input("Please Enter Month Number (1-12):"))

#Checking user output using if - else statement for verifaction
if 1 <= month <= 12:
    print(f"There are {Calendar[month]} day in a month {month}")

else:
    print("Incorrect month number. Please Enter numbers between 1-12.")