a=int(input("enter the first numbers of the series"))
b=int(input("enter the second numbers of the series"))
n=int(input("enter the number of terms needed"))
print(a,b,end="")
while(n-2):
    c=a+b
    a=b
    b=c
    print(c,end="")
    n=n-1
