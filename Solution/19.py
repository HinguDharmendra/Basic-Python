##pyramid

print "Enter the last number in pyramid"
a=int(raw_input())
for i in range(1,a+1):
    l=[]
    j=i
    for j in range(j, i):
        l.append(str(j))
    print l
        
