print("Enter the number you want to find if it is armstrong or not")
a=int(input())
sa=a
s=0
while a!=0:
    
    r=a%10
    s=s+pow(r,3)
    a=a//10
if(sa==s):
    print(f'{sa} is an armstrong number')
else:
    print(f'{sa} is not an armstrong number')