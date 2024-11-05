'''
Write a program that tells a user how many days there are in a specific month. Use a dictionary to map the month numbers (1-12) to the number of days in each month.

### Advanced Requirement:
Leap Year Adjustment: Modify the program to account for leap years. For February, ask the user if the year is a leap year and adjust the number of days accordingly.

'''
#Setting Dictionary
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


#Asking for user input and setting 1-12 as months and if its a leap year

month = int(input("Please Enter Month Number (1-12):"))

#Checking user output using if - else statement for verifaction
if 1 <= month <= 12:
    print(f"There are {Calendar[month]} day in a month {month}")

else:
    print("Incorrect month number. Please Enter numbers between 1-12. ")

#Checking if its a leap year
if  month == 2:
    leap_year = input("Is the current year a leap year? (yes or no) : ").strip().lower()
    if leap_year == "yes":
        print("There are 29 days in this month")
    else:
        print("There are 28 days in this month")
