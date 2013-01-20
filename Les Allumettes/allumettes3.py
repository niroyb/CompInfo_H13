from itertools import izip_longest
import fileinput, sys

def getNbSegmentString(strNb):
    segString = {'0':'1110111','1':'0010010','2':'1011101','3':'1011011','4':'0111010',
                 '5':'1101011','6':'1101111','7':'1010010','8':'1111111','9':'1111011'}
    return ''.join([segString[i] for i in strNb])

def nbMatchMoves(strNb1, strNb2):
    maxPadding = abs(len(strNb1)-len(strNb2)) #DIFFICULTY : Importance of padding ex: 1082
    #Sort by string lenght 
    shortNbStr, longNbStr = sorted([strNb1, strNb2], key = len)
    
    padMoves = []
    #Try all alignments
    for pad  in xrange(maxPadding+1):
        moved = 0
        for pair in izip_longest('0000000'*pad+getNbSegmentString(shortNbStr), getNbSegmentString(longNbStr), fillvalue='0'):
            if pair[0] <> pair[1]:
                moved += 1
        padMoves.append(moved)
    # Return the minimal amount of moves needed to transform strNb1 in strNb2
    return min(padMoves)

def getSolutionAlumette(inputStr):
    strSplit = inputStr.rstrip().split(' ')
    nbStr, nbMoves = strSplit[0], int(strSplit[1])
    #Max nbr of digits of final nb (if adding only ones at the end) (/2 because min of 2 matches to make digit 1)
    maxDigits = len(nbStr)+nbMoves//2
    #Nbr of matches needed per digit
    dicNbMatches = {'0':6, '1':2, '2':5, '3':5, '4':4, '5':5, '6':6, '7':3, '8':7, '9':6}
    #Total nbr of matches available
    nbMatches = sum([dicNbMatches[i] for i in nbStr])
    
    for nb in xrange(int('9'*maxDigits),0, -1):
        combi = str(nb)
        if sum([dicNbMatches[i] for i in combi]) == nbMatches:
            nbDiff = nbMatchMoves(nbStr, combi)
            if nbDiff%2 == 0 and  nbDiff/2 <= nbMoves:
                return combi
    print 'Fail', inputStr

letterEq = fileinput.input().next().rstrip() #reads first line
sol = getSolutionAlumette(letterEq)
sys.stdout.write(sol)
