'''In this exercise, you'll create a simple program that asks the user a question, evaluates their answer, and provides feedback.

### Steps:
1. Write a program that asks the user "What is the capital of France?" and waits for their response.
2. If the user's answer is correct (i.e., "Paris"), the program should print a message saying the answer is correct.
3. If the answer is incorrect, the program should print a message saying the answer is wrong.

'''

#Asking the questions
print("What is the Capital of France?")
answer = input()

#Recieveing and Verifying the answer the answer with if and else
#using .stip and .lower to allow lower cased answers, and .stip will cancel out any indentations

if answer.strip().lower() == "paris":
    print("Correct!")
else:
    print("Incorrect :< , The answer was Paris")    
    