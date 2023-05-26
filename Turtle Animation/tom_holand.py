p=input()
l=len(p)
p1=''
p2=''
j=0
# 4 1 11 10 9 8 7 6 5 3 2
for i in range(l):   

  if p[i] not in p2:
     p2+=p1
     p1=''
     p2+=p[i]+" "

  elif  p[i] in p2:
    p1+=p[i]
    if p1 not in p2:
     p2+=p1+" "
     p1=''

 



 


print(p2)