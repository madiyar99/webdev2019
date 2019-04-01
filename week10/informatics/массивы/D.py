x=int(input())
a = ([int(x) for x in input().split()])
res=sum(i>y for i,y in zip(a[1:],a))
print(res)