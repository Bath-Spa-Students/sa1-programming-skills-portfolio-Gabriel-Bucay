'''
Use your newly acquired knowledge of the for loop to complete the following tasks. Print all values to the console
in each case.
* Write a loop that counts up from 0 to 50 in increments of 1.
* Write a loop that counts down from 50 to 0 in decrements of 1.
* Write a loop that counts up from 30 to 50 in increments of 1.
* Write a loop that counts down from 50 to 10 in decrements of 2.
* Write a loop that counts up from 100 to 200 in increments of 5.
*You may include all loops in a single project*
'''

print("0 to 50 by 1")
#using for loops to count 
for n in range(0, 51, 1):
    print(n)
print("50 to 0 by 1")
for x in range(50,-1,-1):
    print(x)
print("30 to 50 by 1")
for m in range(30,51,1):
    print(m)
for y in range(50,8,-2):
    print(y)
print("100 to 200")
for t in range(100,201,5):
  print(t)
