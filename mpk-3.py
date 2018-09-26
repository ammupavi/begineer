a=[]
n=int(input("enter number of element:"))
for i in range(1,n-1):
    b=int(input("enter smallest  element:"))
    a.append(b)
a.sort() 
print("smallest element is:",a[n-1])   
