'''Write a program that simulates a password entry system. The correct password is defined as 12345. 
The program should keep asking the user to enter the password until they provide the correct one.

### Optional Requirements:

Modify the program to include a maximum of 5 password attempts. If the user enters the wrong password, inform them of the remaining attempts. 
If the maximum number of attempts is reached, inform the user that the authorities have been alerted.
'''
#Setting the password with maximum attempts
Correct_password = "Cogito_Ergo_Sum"
maximum_atempt = 5
attempts = 0


while attempts < maximum_atempt:
    entered_password = input("Please Enter Your Password: ")
    if entered_password == Correct_password:
        print("Welcome back user")
        break
    else:
        #adding 1 to the counter
        attempts += 1
        tries = maximum_atempt - attempts
        if tries > 0:
            print(f"Incorrect Password. {tries} left.")
        else:
            print("You have used up all your Attempts." + '\n' +
                  "THE PO PO HAS BEEN CALLED" + '\n' +
                  "YOU BETTER RUN ")