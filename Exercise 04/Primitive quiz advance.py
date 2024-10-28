'''### Advanced Requirements:
Ignore Capitalization: Modify your program to accept answers regardless of the capitalization (e.g., "paris", "Paris", and "PaRis" should all be considered correct).
Multiple Questions: Extend the program into a quiz that asks for the capitals of 10 European countries. Provide feedback for each question.'''

#using dictionary create the list of countries and capitals

Questions = {
    "France": "Paris",
    "Romania": "Bucharest",
    "Sweden": "Stockholm",
    "Austria": "Vienna",
    "Ireland": "Dublin",
    "Finland": "Helsinki",
    "Denmark": "Copenhagen",
    "Portugal": "Lisbon",
    "Norway": "Oslo",
    "Croatia": "Zagreb"
}

#utilizing loops for the questions
for country, capital in Questions.items(): #looping the questions with for and in
    answer = input(f"What is the Capital of the {country}? ").strip() #asks for the input of the user 
    if answer.strip().lower() == capital.strip().lower(): #verify the answer given
       print("You are correct ^^.")
    else:
        print(f"Incorrect, The answer is {capital}.")
