print("Enter the number you want to find if it is palindrome or not")
n=int(input())
while n!=0:
    a=n
    s=0
    r=n%10
    s=s*10+r
    n=n/10
if a==s:
    print(f'It is an palindrome number')
else:
    print(f'It is not an palindrome number')