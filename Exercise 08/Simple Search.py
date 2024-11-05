'''Write a program that searches for a specific string within a list of strings. 
The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

### Optional Requirements:
1. Allow the user to input the search term instead of using a predefined value.
2. Implement the search functionality based on user input.
'''

#list
targets = ["Jake" "Zac", "Ian", "Ron", "Sam", "Dave"]
targets = set(search_target.strip().lower() for search_target in targets)
search_target = input("Enter the targets name: ")

#if/in loop to search for names
if search_target.strip().lower() in targets:
    print(f"I found you {search_target}!")
else:
    print(f"{search_target} was not found.")

