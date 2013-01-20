import subprocess as sp
import glob, re, os

def  getOutput(args, inputStr):
    #Execute process
    sorter = sp.Popen(args, stdin=sp.PIPE, stdout=sp.PIPE)
    #Send input to created process through stdin
    sorter.stdin.write(inputStr)
    sorter.stdin.close()
    #Obtain output from the created process
    result = sorter.stdout.read()
    return result

def testSuite(program, pathname = ''):
    fileRe = 'in[0-9]*.txt'
    print program
    for filePath in glob.iglob(pathname+fileRe):
        inputStr = open(filePath).read()
        outFileName = pathname+'out'+''.join(re.findall('[0-9]', filePath))+'.txt'
        output = getOutput(['python',pathname+program], inputStr)
        expOutput = open(outFileName).read()
        #print inputStr
        #print output,'---', expOutput

        res = '\tPass' if output == expOutput else '\n'.join(['Fail', output, expOutput])
        print os.path.basename(filePath), res
    print

testSuite('sommeChiffresNombresFinal2.py', 'ChallengeAppelGagnant/')
testSuite('ChooChoo.py', 'ChooChooTrain/')
testSuite('triCount Optimized.py', 'Combien de Triangles/')
testSuite('allumettes3.py', 'Les Allumettes/')
testSuite('CollatzDepth.py', 'Profondeur Collatz/')
