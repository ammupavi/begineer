n=int(input("enter trhe number"))
rev=0
while(n>0)
  dig=n%10
  rev=rev*10+dig
  n=n//10
  print("reverse of the number")
