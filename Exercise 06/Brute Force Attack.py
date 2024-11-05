'''
Write a program that simulates a password entry system. The correct password is defined as 12345. The program should keep asking the user to enter the password until they provide the correct one.

### Basic Requirements:
1. Define the correct password.
2. Use a while loop to repeatedly ask the user for the password until the correct one is entered.
3. Output an appropriate message when the correct password is entered.
'''

#Setting the password
Correct_password = "Cogito_Ergo_Sum"

while True:
    entered_password = input("Please Enter Your Password: ")
    if entered_password == Correct_password:
        print("welcome bback user")
        break
    else:
        print("Incorrect Password, Please Try Again")