'''
Write a program that tests if a value is even or odd. Follow the instructions outlined below:

### Instructions:
* The program should ask the user for a number from within the main function.
* The entered number should be passed to a function that determines if the value is even or odd.
* The function should return a message indicating whether the number is even or odd.
* The message returned by the function should be printed from within the main function.
'''

def is_it_even(number):
    #if else statement to compare for even or odd
    if number %2 == 0:
        return f"This number {number} is even"
    else:
        return f"This number {number} is odd"
    
#Define funtion for user input
def main():
    number = int(input("Please Input a Number: "))
    answer = is_it_even(number)
    print(answer)

if __name__ == "__main__":
    main()



    
    







