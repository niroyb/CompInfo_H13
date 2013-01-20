"""Finds the number of triangles of an input
containing the segment representation of an image"""

__author__ = "Nicolas Roy"

from collections import defaultdict
import sys

lines = sys.stdin.read().splitlines()
mapAdj = defaultdict(set)

#Create optimized adjacency dictionnary
for line in lines:
    nodes = sorted(line)
    for i, node in enumerate(nodes):
        mapAdj[node].update(nodes[i+1:])

count = 0 #Number of triangles
for s1 in mapAdj: #Point 1
    for s2 in mapAdj[s1]: #Point 2
        curLine = [x for x in lines if s1 in x and s2 in x][0] #find start line
        for s3 in mapAdj[s2]: #Point 3
            if s3 in curLine: #exclude flat triangles
                continue
            if s3 in mapAdj[s1]: #is it a triangle
                #print s1,s2,s3
                count += 1
                
sys.stdout.write(str(count))
