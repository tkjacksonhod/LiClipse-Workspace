'''
Created on Nov 2, 2019

@author: ITAUser
'''
i = 2
while i < 6:
    print(i)
    if i == 3:
        break 
    i += 1
fruits = ["apple", "blueberry", "raspberry"] 
for i in fruits:
    print(i) 
n = 5 
for i in range(n):
    for j in range(i): 
        print("*", end = "")
    print("")
