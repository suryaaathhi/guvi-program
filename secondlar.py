N=int(input())
a=[]
for i in range(1,N+1):
    M=int(input())
    a.append(M)
    a.sort()
if a[0]>a[1]:
    print(a[0])
else:
    print(a[1])
