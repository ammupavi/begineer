num=int(input("enter the value of n:")) 
hold=num
sum=0
if num <=0:
  print("enter a natural positive number!")
else:
  
  while num >0:
    sum=sum+num
    num=num-1;
    print(" sum of  first ",hold,"natural number is:",sum)

