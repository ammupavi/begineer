from constraint import*
probelm=problem()
problem.add variable('a',range(5))
problem.add variable('b',range(5))
problem.addconstraint(lambda.a,b:a+b==5)
problem.addconstraint(lambda.a,b:a*b==6)
problem.get solution()
