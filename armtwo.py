val1=int(input())
val2=int(input())
for num in range(val1,val2+1):
    s=0
    temp=num
    while(temp>0):
        dig=temp%10
        s=s+dig**3
        temp=temp//10
    if(num==s):
        print(num)
