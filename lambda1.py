# adder= lambda a, b:a-b
# print(adder(67,12))

# a=list(range(10,24,1))
# print(a)
# #map(logic, variable)
 
# x=list(map(lambda x:x**2,a))
# print(x)

# even=list(map(lambda x :x%2 ==0,a))
# print(even)

# even_no=list(filter(lambda  x :x%2 ==0,a))
# print(even_no)

# age=list(map(lambda x:int(x),input("enter frnds age:").split()))

# print(age) 
# # list,dict,set comprehensions
# # desired_output define_iterative_operation(loop) conditionals

# x=[i**2 for i in a]
# print(x)

# y=[list(filter(lambda x:x%2==0 , a))]
# print(y)

a=list(range(10,15))
b=list("ABCDE")
print(a,b)
q={i:j for i,j in zip(a,b)}
print(q)

z={i for i in q.keys()}
print(z)