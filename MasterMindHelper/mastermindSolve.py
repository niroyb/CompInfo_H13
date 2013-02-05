from itertools import product
import sys

COLORS = (1,2,3,4,5,6)

def getInitSolPool():
    return [prod for prod in product(COLORS, repeat=4)]

def getBlackWhiteVal(guessed, reference):
    '''Returns the number of correctly placed pegs and the number of wrongly placed pegs'''
    guess = list(guessed)
    ref = list(reference)
    correct = 0
    badPos = 0
    for i in xrange(len(guess)):
        if guess[i] == ref[i]:
            ref[i] = -1
            guess[i] = -1
            correct += 1
    for i in guess:
        if i >= 0 and i in ref:
            badPos += 1
            ref.remove(i)
    return (correct, badPos)

def getFilteredPool(solPool, guess, blackWhiteVal):
    '''Returns a solution pool filtered with the gained info'''
    return [sol for sol in solPool if getBlackWhiteVal(sol, guess) == blackWhiteVal]

def getSolutionMasterMind(text):
    game = []
    solPool = getInitSolPool()
    lines = text.splitlines()
    for line in lines:
        trieStr, guessStr = line.split()
        trie = map(int, trieStr)
        result = map(int, guessStr)
        solPool = getFilteredPool(solPool, trie, result)
        if len(solPool) == 0:
            return 'Il y a une erreur de logique!'
    return str(len(solPool))

if __name__ == '__main__':
    inp = sys.stdin.read()
    print inp
    sys.stdout.write(getSolutionMasterMind(inp))
