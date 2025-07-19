shopping=["egg","Butter","bread"," spices","coke"]
length=len(shopping)
print(f' length of the entered shopping list is {length}') # length is 5 because there are 5 items in the shopping which is a list function


# in list it is same as array[in c program] in which the first can be accessed by 0 and so on
print(shopping[0]) # prints egg
print(shopping[1]) # prints butter
print(shopping[2]) # prints bread

#wap to enter the list and print it one after another
print('Enter the name of the students that you want to repeat')
for i in range (5):
    list[i]=str(input())
for i in range (5):
    print(list[i])