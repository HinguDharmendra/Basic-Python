#pythagorean triads
import math
def pythagorean_triads():
        aa=[]
        bb=[]
        cc=[]
        atrue=False
        btrue=False
        ctrue=False
        for  a in range(1,101):
                for b in range(1,101):
                        for c in range(1,142):
                                if(a<b):
                                        if(c==math.sqrt(a*a+b*b)):
                                                aa.append(a)
                                                bb.append(b)
                                                cc.append(c)
                                                if(not (a/2 in aa and b/2 in bb and c/2 in cc)):
                                                        print [a, b, c]
pythagorean_triads()

##Output:
##[3, 4, 5]
##[5, 12, 13]
##[7, 24, 25]
##[8, 15, 17]
##[9, 12, 15]
##[9, 40, 41]
##[11, 60, 61]
##[12, 35, 37]
##[13, 84, 85]
##[15, 20, 25]
##[15, 36, 39]
##[16, 63, 65]
##[20, 21, 29]
##[20, 99, 101]
##[21, 28, 35]
##[24, 45, 51]
##[25, 60, 65]
##[27, 36, 45]
##[28, 45, 53]
##[33, 44, 55]
##[33, 56, 65]
##[35, 84, 91]
##[36, 77, 85]
##[39, 52, 65]
##[39, 80, 89]
##[40, 75, 85]
##[45, 60, 75]
##[48, 55, 73]
##[51, 68, 85]
##[57, 76, 95]
##[60, 63, 87]
##[60, 91, 109]
##[63, 84, 105]
##[65, 72, 97]
##[69, 92, 115]
##[75, 100, 125]		