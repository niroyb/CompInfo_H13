#Nicolas Roy - 13 Janvier 2013
import re, sys, string, itertools

def yieldSolutions(letterEq):
    letterEq = letterEq.replace('=', '==')
    letters = re.sub('[^a-zA-Z]', '', letterEq)
    diffLetters = []
    for let in letters:
        if let not in diffLetters:
            diffLetters.append(let)
    diffLetters = ''.join(diffLetters)
    assert len(diffLetters) <= 10
    leadZero = re.compile('[^0-9]0')

    for perm in itertools.permutations('0123456789', len(diffLetters)):
        transTab = string.maketrans(diffLetters, ''.join(perm))
        nbFormula = letterEq.translate(transTab)
        if nbFormula[0] <> '0' and not leadZero.search(nbFormula) and\
           eval(nbFormula) == True:
            yield nbFormula.replace('==', '=')#, diffLetters.translate(transTab)

letterEq = raw_input()
sol = yieldSolutions(letterEq).next() #get first solution
sys.stdout.write(sol)
