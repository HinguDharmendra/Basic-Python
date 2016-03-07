###Kaprekar's constant
num=raw_input()
#print list(map(int,str(num)))
#print ''.join(splits(num))
lis=list(map(int,str(num)))
a=[]
d=[]
a=sorted(lis)
b=sorted(lis, reverse=True)
num = int(''.join(b)) - int(''.join(a))

print num
