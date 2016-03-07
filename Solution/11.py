## perfect square and even digits
import math
def divide(n):
    lis=[]
    while(n>0):
        lis.append(n%10)
        n/=10
    return lis

def evendig_perfect(n, m):
    li=[]
    for i in range(n, m ,2):#considers only even numbers in range
        number=True
        l=divide(i)
        for k in l:
            if(k%2!=0):
                number=False
                break
        if(number==True):
            if(math.sqrt(i).is_integer()==True):
                li.append(i)

    print li

evendig_perfect(1000, 10000)
    
##Output:
##[4624, 6084, 6400, 8464]
