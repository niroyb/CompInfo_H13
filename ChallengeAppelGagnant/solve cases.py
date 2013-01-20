
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

with open('AllCases.txt') as f:
    cases = f.read().splitlines()
    #print cases
with open('AllCasesSolved.txt', 'w') as outf:
    for case in cases:
        sol = getOutput(['python', 'sommeChiffresNombresFinal2.py'], case)
        outf.write(case+'\t'+sol+'\n')
