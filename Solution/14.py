##calculate bishop moves from(x, y)

def bishop(x, y):
    x1,x2,x3 = x,x,x
    y1,y2,y3 = y,y,y
    while(x1<8 and y1<8):
        x1+=1
        y1+=1
        print x1, y1

    while(x2>1 and y2>1):
        x2-=1
        y2-=1
        print x2, y2

    while(x3>1 and y3<8):
        x3-=1
        y3+=1
        print x3, y3

    while(x<8 and y>1):
        x+=1
        y-=1
        print x, y
        
print "Enter the current position of bishop"
print "x:"
x=int(raw_input())
print "y:"
y=int(raw_input())
print "Possible moves could be"
bishop(x, y)

##Output:
##Enter the current position of bishop
##x:
##3
##y:
##3
##Possible moves could be
##4 4
##5 5
##6 6
##7 7
##8 8
##2 2
##1 1
##2 4
##1 5
##4 2
##5 1
