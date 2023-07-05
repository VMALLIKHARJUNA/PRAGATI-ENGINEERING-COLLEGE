L=[1,2,3]
r=map(lambda x:x+x,L)
print(list(r))
#map-helps to create iteration,it returns map obj
res =map(lambda n:pow(n,2),L)
print(list(res))
name="sam"
(lambda name:print(name))(name)