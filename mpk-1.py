def sumofAP(a,n,d):
    sum=0
    i=0
    while i < n:
        sum =sum+a
        a=a+d
        i=i+1
    return sum    
