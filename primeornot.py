val1=int(input())
if(val1>1):
    for i in range(2,val1):
        if(val1%i==0):
            print("no")
            break
        else:
            print("yes")
            break
