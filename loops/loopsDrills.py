'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''
#EX) Declare a variable set to 3. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 0.
i = 3;
while i > 0:
    print(i)
    i -= 1

'''
END OF EXAMPLE
'''

'''
START HERE
'''

'''While Loops'''
#1) Declare a variable set to 4. Make a while loop that prints the variable 
#    you just created and decrements the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 1.
i = 4 
while i > 1:
    print(i)
    i -= 1
#2) Declare a variable set to 14. Make a while loop that prints the variable 
#    you just created and increments the variable by one each time through
#    the loop. Meanwhile, make the loop run until the variable you created 
#    equals 20.
i = 14
while i > 20: 
    print(i) 
    i += 1
#3) Declare a variable set to 55. Make a while loop that prints the variable 
#   you just created. Then make an if statement that makes the loop break when
#   the variable is equal to 50. 
i = 55
while i > 0:
    print(i)
    if i == 50:
        break
    i -= 1 
'''For Loops'''
#4) Create a list named sports. Put three sports into the list. Create
#   a for loop that prints each sport in the list
sports = ["soccer", "football", "volleyball"]
for i in sports:
    print(i) 
#5) Create a for loop that loops through each letter in a string of one of your
#   favorite songs. Each iteration should print should a letter of the word. 
song = ["t","i","n","t","s"]
for i in song:
    print(i) 
#6) Create a list named movies. Put five of your favorite movies into the list.
#   However, make sure one of the movies is Avatar. 
#   Create a for loop that iterates over the list. In the loop print the movie
#   being looped over, but create an if statement that breaks out of the 
#   loop if it is Avatar.
movies = ["avatar", "grease", "labyrinth", "dirty dancing", "coraline"]
for i in movies:
    print(i) 
    if i == "avatar":
        break 