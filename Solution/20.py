##range to numbers
print "Enter the string"
a=raw_input()
lis=a.split(',')
l=[]
string=[]
for i in lis:
    l.append(i.split('-'))

##print l1, l1[1]
for i in l:
    if(len(i)>1):
        for k in range(int(i[0]), int(i[1])+1):
            string.append(k)
    else:
        string.append(int(i[0]))

print string

##Output:
##Enter the string
##1, 3-7, 12, 15, 18-21
##[1, 3, 4, 5, 6, 7, 12, 15, 18, 19, 20, 21]
    
