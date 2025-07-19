def sum(n):
 s=0
 for i in range(0, n+1):
        s+=i
 return s
print("enter the number till you want sum using function")
n=int(input())
r=sum(n)
print(f'sum till {n} is {r}')
    