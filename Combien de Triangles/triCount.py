import fileinput, sys

lines = []
for line in fileinput.input():
    lines.append(line.rstrip())

mapAdj = {}

#print lines
for line in lines:
    for letter in line:
        for letter2 in line:
            if letter <> letter2:
                mapAdj.setdefault(letter, set()).add(letter2)
keys = sorted(mapAdj.keys())
'''
print 'Matrice d\'adjacence :'
for key in keys:
    print key, ':',''.join(sorted(mapAdj[key]))
print '\nTriangles :'
'''

count = 0
for s1 in keys: #sommet 1
    for s2 in sorted(mapAdj[s1]): #sommet 2
        if ord(s2) <= ord(s1): #prevent triple counting
            continue
        curLine = [x for x in lines if s1 in x and s2 in x][0] #find start line
        for s3 in sorted(mapAdj[s2]): #sommet 3
            if ord(s3) <= ord(s2) or s3 in curLine: #exclude flat triangles
                continue
            if s1 in mapAdj[s3]: #is it a triangle
                #print s1,s2,s3
                count += 1
sys.stdout.write(str(count))
