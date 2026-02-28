def fibtab(n):
    a=[0,1]
    for i in range(2,n+1):
        x=a[i-1]+a[i-2]
        a.append(x)
    return a 
n=int(input("enter the number"))
print(fibtab(n))
