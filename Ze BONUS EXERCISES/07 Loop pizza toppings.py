'''
Loop pizza toppings:
Write a loop that prompts the user to enter a series of pizza toppings until they enter a
'quit' value. As they enter each topping,
Print a message saying you'll add that topping to their pizza.
'''

#creating loop with user input
while True: #while loops to loop question until keyword 'quit'
    toppings_choice = input("Please Enter your toppings of choice (use quit to stop): ")
    
    
    #confirmation from user
    if toppings_choice.lower() == 'quit':
        print("Finishing up topping selection")
        break
    if not toppings_choice:
        print("You didnt enter anything. Please try again.")

    print(f"Great! adding {toppings_choice} to your pizza.")

#Confirm the user for each topping
    confirm = input("Confirm order with this topping? (yes/no): ").strip().lower()

    if confirm == 'yes':
        print(f"Adding {toppings_choice} to your pizza.")
    elif confirm == 'no':
        print("Let's try again with a different topping.")
        continue  # Repeats the loop, allowing the user to choose another topping
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")