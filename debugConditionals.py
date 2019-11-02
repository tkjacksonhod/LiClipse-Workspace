'''For this assignment you should look at the variables create below and find the error.
For each task, there will be one error that you must find and correct.
Sometimes there will be an explanation of the problem and/or tips 
that can help you complete the tasks.'''

#1)
#Broken:
#x = 2
#y = 8
#if x < y
#    st = "x is less than y"
#print(st)
#Correct:
x = 2
y = 8
if x < y:
    st = "x is less than y"
    print(st)

#2)
#Broken:
#x = 2
#y = 8
#if x < y
#    st = "x is less than y"
#else:
#st = "x is greater than y"
#print(st)
#Correct:
x = 2
y = 8
if x < y:
    st = "x is less than y"
else:
    st = "x is greater than y"
    print(st)

#3)
#Broken:
#age = 
#if age < 0:
#   print "This can hardly be true!"
#   elif age == 1:
#   print "about 14 human years"
#   elif age == 2:
#   print "about 22 human years"
#   elif age > 2:
#   human = 22 + (age -2)*5
#   print "Human years: ", human
age = 12
human = 22 + (age -2)*5
if age < 0:
    print "This can hardly be true!"
elif age == 1:
    print "about 14 human years"
elif age == 2:
    print "about 22 human years"
else:
    print("Human years", human)

