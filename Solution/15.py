#pyramid

print "Enter the no. lines"
a=int(raw_input())

for i in range(1, a+1):     #for each i no. of * is 2i-1
    l=[]
    for j in range(a-1, 0, -1):
        if(j>=i):
            l.append(" ")
    for k in range(1, 2*i):
            l.append("*")
    print ''.join(l)

##Output:
##Enter the no. lines
##4
##   *
##  ***
## *****
##*******


    
