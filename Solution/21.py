print "Enter Date"
def mnth(string):
    mapp={'janauary':1, 'february':2, 'march':3,'april':4, 'may':5, 'june':6,
          'july':7, 'august':8, 'september':9, 'october':10, 'november':11,
          'december':12}
    return mapp[string]

a=raw_input()
l=[]
l1=[]
if(',' in a):
    l1=a.split(',')
    l=l1[1].split()
    l.insert(0,l1[0])
else:
    l=a.split()

t=(int(l[-1]), mnth(l[-2]), int(l[-3]))
print t

##Output:
##Enter Date
##29 june 2013
##(2013, 6, 29)
