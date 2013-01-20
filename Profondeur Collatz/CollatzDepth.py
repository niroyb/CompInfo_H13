"""Finds how many numbers take n steps to reach 1 with
the Collatz conjecture"""
__author__ = "Nicolas Roy"

from sys import stdout

def getReverseCollatz(n):
    '''Returns the number(s) that give n following
    one iteration of the Collatz conjecture'''
    if n == 4:
        return (8,)
    if n%6 == 4:
        return 2*n, (n-1)/3
    else:
        return (2*n,)

def getCollatzDepth(n):
    '''Returns the number(s) that take exactly n
    iterations of the Collatz conjecture to reach 1'''
    old = [1]
    for _ in xrange(n):
        new = []
        for o in old:
            new += getReverseCollatz(o)
        old = new
    return old

ans = len(getCollatzDepth(int(raw_input())))
stdout.write(str(ans))
