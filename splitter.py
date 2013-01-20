

def splitTestFile(fileName, filePath = ''):
    for i, line in enumerate(open(filePath+fileName).read().splitlines()):
        print i, line
        inp, outp = line.split('\t')
        with open(filePath+'test_in_'+str(i)+'.txt', 'w') as testInput:
            testInput.write(inp)
        with open(filePath+'test_out_'+str(i)+'.txt', 'w') as testOutput:
            testOutput.write(outp)
    

splitTestFile('ChooChooTrain Tests.txt', 'ChooChooTrain/')
splitTestFile('Les Allumettes Tests.txt', 'Les Allumettes/')
splitTestFile('AllCasesSolved.txt', 'ChallengeAppelGagnant/')
splitTestFile('Cases.txt', 'Profondeur Collatz/')
