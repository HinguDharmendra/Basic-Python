##Pyramid
print "Enter the lines"
a=int(raw_input())

for i in range(1, a+1): ##for each line no. of * is equal to line number
    l=[]
    for j in range(a-i, 0, -1):
        l.append(" ")
    for k in range(1, i+1):
        l.append(" * ")
    print ' '.join(l)

##Output:
##Enter the lines
##5
##         * 
##       *   * 
##     *   *   * 
##   *   *   *   * 
## *   *   *   *   *
