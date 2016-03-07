## pyramid

print "Enter no. of lines"
a=int(raw_input())
for i in range(1, a+1):
    l=[]
    for j in range(i, i*i+1, i):
        
        l.append(str(j)+' ')
    print ' '.join(l)
        
