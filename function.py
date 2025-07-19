
def sum():
    s = 0
    for i in range (1, 1000):
      s+=i
    return s

print("enter how many times you want the function to call")
a=int(input())
for i in range (a):
  result=sum()
  print(f" sum is: {result}")
