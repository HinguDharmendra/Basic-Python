##amicable this has taken so long try to minimize the execution

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

def amicable(n, m):
    for i in range(n, m+1):
        if(aliquot(aliquot(i))==i):
            print [i, aliquot(i)]

amicable(10000, 1000000)
