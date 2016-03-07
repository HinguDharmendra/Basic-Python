#armstrong
num=100
while(num<=999):
    x=num
    s=0
    while(x>0):
        p=x%10
        s=s+p**3
        x=x/10
    if(s==num):
        print num

    num=num+1
    
#Output:
#153
#370
#371
#407
