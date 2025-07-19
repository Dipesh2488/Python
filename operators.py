# # #airthematic operator 
# a=123nad as boolean gat
# a+=3    #a=a+3
# print(f"new value of a is {a}") 
# b=120
# s=a-b
# A=a+b
# d=a/b
# m=a%b
# print(f"subtraction is {s}")    #output=6
# print(f"addition is {A}")  
# print(f"Division is {d}")
# print(f" mode is {m}")

# #comparison operator
# x=10
# y=20
# s=x==y  
# z=x<y  
# print(f"z is {z}")  # output=true
# print(f's is {s}')  #output false

# other comparison operator are <,>,<=,>=,!= etc..

#logical operators  [or , and, not] can be used with comparison operators

#or operator
b3 = not 5 == 4 or 5 == 2 
print(b3) #output true

#and operator
b1 = (5 > 3) and (1 == 1) 
print(b1) #output true

#not operator
b2 = not (3 > 4) 
print(b2) #output true

# can be used as boolean algebra gates
b1 = True
b2 = True
b3 = False

b4 = b1 and b2 and (not b3)
print(f"b4 = {b4}") #output=true{ calculation as boolean algebra}




