import sys


def getCollatzNb(depth):
    if depth == 0:
        return [1]
    seen = {0,1}
    toTreat = [1]
    newNb = []
    for d in xrange(depth):
        newNb = []
        for nb in toTreat:
            div, mod = divmod(nb-1,3)
            if mod == 0 and div%2 == 1:
                newNb.append(div)
            newNb.append(2*nb)
        toTreat = []
        for nb in newNb:
            if nb not in seen:
                toTreat.append(nb)
            seen.add(nb)
        #sys.stdout.write(str(d+1)+'\t'+str(len(toTreat))+'\n')
        #print d+1, len(toTreat)
    return toTreat

def getDepth(n):
    x = 0
    while n > 1:
        if n&1:
            n = 3*n+1
        else:
            n = n>>1;
        print n
        x = x + 1
    return x

#print getDepth(8)

#for i in xrange(10):
#    print i, len(getCollatzNb(i)), getCollatzNb(i)

#print getDepth(11)
sys.stdout.write(str(len(getCollatzNb(int(raw_input())))))
#print len(getCollatzNb(60))
#getCollatzNb(15)

#f = open('toto.txt', 'w')
#f.write(' '.join(map(str,sorted(getCollatzNb(50)))))
#f.close()
