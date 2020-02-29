'''
For this assignment you should read the task, then below the task do what it asks you to do
based on what the task tells you do first.
EXAMPLE TASK:
'''

'''
START HERE
'''

'''Write a File'''
#1) Create a file with Python that is named after your first and last name.  
#   Then write your first name on the first line with Python and your last name
#   on the second line with Python. 
#    
file1 = open("TrinityJacksonHodges.txt", "a")
line = ["Trinity", "Jackson-Hodges"]
file1.writeLines(line)
file1.close()
#2) In the same file you just created describe one of the projects you created
#   with at least 5 lines and how you think you can improve.
#    
#    
file1 = open("TrinityJacksonHodges.txt", 'w')
line = ["A project I made was hangman", "You had to guess letters of the word", "There was a specfic set of words", "I could improve by being more creative", "I also could add more words next time"]
file1.writeLines(line) 
#3) Within 5 lines of the previous lines you've written on, describe what line 
#   you are on, on that line. Then close the file
#    

'''Read a file'''
#4) Open the previous file you created. Create an if statement that checks if
#   the mode is r. If the mode is r, create a variable named contents and set
#   the variable with .read() of the file you created. Print the contents of
#    the file. Close the file
file1 = open("TrintyJacksonHodges.txt", 'r')
if mode = "r":
    then x= contents.read()
    print(x)
    file1.close() 
#5) Open the same file you created. Create a variable that uses .readLines() of
# the file Create a for loop that prints each line in the file.
file1 = open("TrinityJacksonHodges", 'r')
y = file1.readLines() 
file1.close() 
for i in len(y):
    print(y(i))
#6) Print the first, middle, and last line in the file.
file1 = open("TrinityJacksonHodges", 'r')
y = file1.readLines() 
print(y(0))
print(y(2))
print(y(4))


