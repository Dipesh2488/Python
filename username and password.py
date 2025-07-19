def sigma(username, password):
    if username=='user' and password=='qweasd':
        return True
    else:
        return False
    if username=='admin' :
        return True
    else:
        return False
print("enter your username")
username=str(input())
print("enter your password")
password=str(input())
re=sigma(username, password)
print(re)