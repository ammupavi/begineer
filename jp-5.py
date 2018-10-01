def countdigits(a,b)
 count=0
 if(p==0):
   return 1
 while(p>0):
    count=count+1
    p=p//10
    return count
 a=56
 b=-54
 print("number of digits=",countdigit(a,b))
