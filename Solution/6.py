#collatz sequence
print "Enter random number(Integer) - "
num=int(raw_input())
lis=[]
lis.append(num)
l=0
while(l<10):
    if(num%2==0):
        num=num/2
        lis.append(num)
    if(num%2!=0):
        num=num*3 + 1
        lis.append(num)
    if(len(lis)>3):
        if(lis[-1]==1 and lis[-2]==2 and lis[-3]==4):
            break;
    l+=1

print lis
