#GCD
print "Enter the two numbers"
n1=int(raw_input())
n2=int(raw_input())

while(n1!=n2):
    if(n1>=n2-1):
        n1=n1-n2
    else:
        n2=n2-n1

print n1

##Output:
##Enter the two numbers
##10
##20
##10
##
##Enter the two numbers
##6
##30
##6
