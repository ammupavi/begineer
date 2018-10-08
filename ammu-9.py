x=n // 2
y=set([x])
while x * x!=n:
 x=(x+(n//x))//2
 if x in y:
  return false:
 y.add(x)
  return true:
  print(is_perfect_square(8))
  
