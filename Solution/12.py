##aliquot number
def summation(lis):
    s=0
    for i in lis:
        s=s+i
    return s 
def aliquot(n):
    l=[]
    for i in range(1, n):
        if(n%i==0):
            l.append(i)
    return summation(l)


print "Enter number"
x=int(raw_input())
print aliquot(x)

#Output:
#Enter number
#12
#16
