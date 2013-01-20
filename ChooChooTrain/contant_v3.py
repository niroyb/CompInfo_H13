# Felix Contant
# Competition Informatique 2013
# ChooChooTrain
# v2


from random import choice
import time
import re, sys
from multiprocessing import Process, Pipe

MAX_DURATION = 4.7
OPERATORS = ('+', '-', '*', '=', ' ')
NB_PROCESS = 15

def makeUnique(lst):
    #source : http://www.peterbe.com/plog/uniqifiers-benchmark
    seen = set()
    seen_add = seen.add
    return [x for x in lst if x not in seen and not seen_add(x)]


def combine(list):
    return ''.join(str(val) for val in list)


def transformToExpressions(words):
    lst = []
    for w in words:
        if w not in OPERATORS:
            exp = '(' + w + ')'
            lst.append(exp)
        else:
            lst.append(w)
    return lst


def permutations(lst):
    # source : http://code.activestate.com/recipes/252178/
    remove = lambda lst0, index: lst0[:index] + lst0[index + 1:]
    if lst:
        for index, x in enumerate(lst):
            for y in permutations(remove(lst, index)):
                yield (x,) + y
    else:
        yield ()


def permutationsDepth(lst, depth):
    # source : http://code.activestate.com/recipes/252178/
    remove = lambda lst0, index: lst0[:index] + lst0[index + 1:]
    if lst and depth > 0:
        for index, x in enumerate(lst):
            for y in permutationsDepth(remove(lst, index), depth - 1):
                yield (x,) + y
    else:
        yield ()


def testAll(inputLine):
    line = inputLine
    words = re.findall(r'\w+', line)
    letters = makeUnique([w[0] for w in line if w not in OPERATORS])
    firstLetters = makeUnique([w[0] for w in words if w[0] not in OPERATORS])
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Decorating words with ()
    line = '(' + line + ')'
    line = line.replace('+', ')+(')
    line = line.replace('-', ')-(')
    line = line.replace('*', ')*(')
    line = line.replace('=', ')=(')
    #Decorating letters with {0[A]} for futur evaluation
    for l in letters:
        line = line.replace(l, '{0[' + l + ']}')

    parts = line.split("=")
    leftPart = parts[0]
    rightPart = parts[1]
    totalNbTry = 0
    nbTryRequired = 0
    bestSol = ''
    mem = {}

    # Testing all possible values
    for v in permutationsDepth(values, len(letters)):
        totalNbTry += 1
        randomVals = {}
        for i in range(len(letters)):
            randomVals[letters[i]] = v[i]

        flag = False
        for k in randomVals.keys():
            if k in firstLetters and randomVals[k] == 0:
                flag = True
        if flag:
            continue

        # Placing numbers in the string
        tryLeftPart = leftPart
        tryRightPart = rightPart
        for l in randomVals.keys():
            tryLeftPart = tryLeftPart.format(randomVals)
            tryRightPart = tryRightPart.format(randomVals)

        # Saving calculations
        if tryLeftPart not in mem:
            mem[tryLeftPart] = eval(tryLeftPart)
        if tryRightPart not in mem:
            mem[tryRightPart] = eval(tryRightPart)

        # Test solutions
        if mem[tryLeftPart] == mem[tryRightPart]:
            solLine = inputLine
            for l in randomVals.keys():
                solLine = solLine.replace(l, str(randomVals[l]))
            if solLine < bestSol or bestSol == '':
                bestSol = solLine
                nbTryRequired = totalNbTry
    if bestSol == '':
        print 'Not Found!'
    else:
        sys.stdout.write(bestSol.rstrip())
    # Debug
    #print 'totalNbTry : ', totalNbTry
    #print 'nbTryRequired : ', nbTryRequired


def testRandom(inputLine, allowedTime, conn):
    startTime = time.time()
    line = inputLine
    words = re.findall(r'\w+', line)
    letters = makeUnique([w[0] for w in line if w not in OPERATORS])
    firstLetters = makeUnique([w[0] for w in words if w[0] not in OPERATORS])
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    #Decorating words with ()
    line = '(' + line + ')'
    line = line.replace('+', ')+(')
    line = line.replace('-', ')-(')
    line = line.replace('*', ')*(')
    line = line.replace('=', ')=(')
    #Decorating letters with {0[A]} for futur evaluation
    for l in letters:
        line = line.replace(l, '{0[' + l + ']}')

    parts = line.split("=")
    leftPart = parts[0]
    rightPart = parts[1]
    totalNbTry = 0
    nbTryRequired = 0
    bestSol = ''
    mem = {}

    while True:
        # Execution timing control
        totalNbTry += 1
        if totalNbTry % 2 ** 15:
            if time.time() - startTime > allowedTime:
                break

        # Generating random values
        randomVals = {}
        availableValues = values[:]
        flag = False
        for l in letters:
            val = choice(availableValues)
            if val != 0:
                availableValues.remove(val)
            else:   # is zero
                if l not in firstLetters:
                    availableValues.remove(val)
                else:
                    flag = True
                    continue
            randomVals[l] = val

        if flag:
            continue

        # Placing numbers in the string
        tryLeftPart = leftPart
        tryRightPart = rightPart
        for l in randomVals.keys():
            tryLeftPart = tryLeftPart.format(randomVals)
            tryRightPart = tryRightPart.format(randomVals)

        # Saving calculations
        if tryLeftPart not in mem:
            mem[tryLeftPart] = eval(tryLeftPart)
        if tryRightPart not in mem:
            mem[tryRightPart] = eval(tryRightPart)

        # Test solutions
        if mem[tryLeftPart] == mem[tryRightPart]:
            solLine = inputLine
            for l in randomVals.keys():
                solLine = solLine.replace(l, str(randomVals[l]))
            if solLine < bestSol or bestSol == '':
                bestSol = solLine
                nbTryRequired = totalNbTry

    if bestSol == '':
        conn.send(('Not Found!', totalNbTry, nbTryRequired))
    else:
        conn.send((bestSol, totalNbTry, nbTryRequired))
    conn.close()
    # Debug
    #print 'Time Process : ', time.time() - startTime
    #print 'totalNbTry : ', totalNbTry
    #print 'nbTryRequired : ', nbTryRequired


if __name__ == '__main__':
    startTime = time.time()
    inputLine = raw_input().rstrip()
    line = inputLine
    words = re.findall(r'\w+', line)
    letters = makeUnique([w[0] for w in line if w not in OPERATORS])
    if len(letters) < 8:
        testAll(inputLine)
    else:
        #Multiple process
        ps = []
        pipes = []
        for i in range(NB_PROCESS):
            parent_conn, child_conn = Pipe()
            allowedTime = MAX_DURATION - (time.time() - startTime)
            p = Process(target=testRandom, args=(inputLine, allowedTime, child_conn))
            ps.append(p)
            pipes.append(parent_conn)
            p.start()

        res = []
        totTry = 0
        for i in range(NB_PROCESS):
            r = pipes[i].recv()
            totTry += r[1]
            res.append(r[0])
        sys.stdout.write(min(res).rstrip())
        #print min(res)
        #print totTry

   #print 'Time Total : ', time.time() - startTime
