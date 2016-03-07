##number pyramid
print "Enter the depth"
level=int(raw_input())
print '\n'
for i in range(1,level+1):
    lis=[]
    for j in range(1,i+1):
        lis.append(str(i)+" ")
    print ''.join(lis)


##Output:
##Enter the depth
##7
##
##
##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5 
##6 6 6 6 6 6 
##7 7 7 7 7 7 7 
       

