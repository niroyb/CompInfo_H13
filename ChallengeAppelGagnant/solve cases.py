
import subprocess as sp

def  getOutput(args, inputStr):
    #Execute process
    sorter = sp.Popen(args, stdin=sp.PIPE, stdout=sp.PIPE)
    #Send input to created process through stdin
    sorter.stdin.write(inputStr)
    sorter.stdin.close()
    #Obtain output from the created process
    result = sorter.stdout.read()
    return result

with open('AllCases.txt') as f:
    cases = f.read().splitlines()

with open('AllCasesSolved.txt', 'w') as outf:
    args = ['python', 'sommeChiffresNombresFinal2.py']
    for case in cases:
        sol = getOutput(args, case)
        outf.write(case+'\t'+sol+'\n')
