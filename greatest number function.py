def max(n1, n2):
  if n1 > n2:
   return n1
  else:
    return n2
print("To find greatest number")
n1=int(input("first number :  "))
n2=int (input("second number :  "))
re=max(n1, n2)

print(f"{re} is greater")
