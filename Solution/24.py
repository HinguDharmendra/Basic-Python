##range to numbers
#after 10 check it out
print "Enter the string"
a=raw_input()
lis=a.split(',')
l=[]
string=[]
for i in lis:
    l.append(i.split('-'))

for i in l:
    if(len(i)>1):
        for k in range(int(i[0]), int(i[1])+1):
            string.append(k)

print string


##Output:
##Enter the string
##4-7, 9, 12, 15
##[4, 5, 6, 7]
