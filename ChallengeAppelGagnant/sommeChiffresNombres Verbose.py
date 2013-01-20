from re import findall
from itertools import product

def substrings(string):
    j=len(string)
    ret = []
    while True:
        for i in range(len(string)-j+1):
            ret.append(string[i:i+j])
        if j==1:
            break
        j-=1
        #string=string[1:]
    return ret

#http://code.activestate.com/recipes/81611-roman-numerals/
numeral_map = zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

def int_to_roman(i):
    result = []
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n):
    n = unicode(n).upper()
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    #DANGER: Return value only if valid roman numeral
    if n == int_to_roman(result):
        return result
    else:
        return 0

def digitalVal(item):
    arr = []
    dico = {'0':['0','1','7'], '1':['1'], '2':['2'], '3':['1','3','7'], '4':['1','4'], '5':['5'],'6':['5','6'],
            '7':['1','7'], '8':['0','1','2','3','4','5','6','7','8','9'], '9':['1','3','4','5','7','9']}
    for subStr in substrings(item):
        lists = [dico[n] for n in subStr]
        #print lists
        #DIFFICULTY: Generate arbitrary size cartesian product
        for combination in product(*lists):
            strCombi = ''.join(combination)
            #DANGER: Do not count combinations starting with 0
            if strCombi[0] <> '0':
                #print combination, strCombi
                arr.append(int(strCombi))
            else:
                arr.append(0)
    #print 'digitalVal', item, substrings(item), som
    return arr

def numbrVal(item):
    arr = [int(i) for i in substrings(item) if i[0] <> '0'] #DANGER: Do not count combinations starting with 0
    #print 'numbVals:', substrings(item), 'val=',val
    return arr

def romanVal(item):
    #print 'romans:', substrings(item), 'val=',val
    return map(roman_to_int, substrings(item))

def otherVal(item):
    dico = {'-':[1], '=':[1,1,2]}
    return dico[item]

#inp = '4+(15+1)X2+#82-(7X0+I6)+25-4X2+C+L+L=MILAKUNIS'
#inp = 'C1 2+32C X L C+L+_+LI+#8X(5+1X13)=2'

#inp = 'L+(2X#8+3)+23-I2+(II X4+2)+14+(18-II)+5+7= AVRIL LAVIGNE'
#inp = 'L+(2X#8+3)+2 3-I2+(II X4+2)+14+(18-11)+5+7=? AVRIL LAVIGNE'
#inp = '(2+4)X5+1-_+L+8X#18+1X2=2 CAROL 69'
#inp = 'L+L+9+9+7X0-1 6-3+3+3-C4+5C+3+2+I+I' #IG got wrong answer lol
#inp = 'L+L+C6/3C X5/8/7-61-#35X8-C4-3X9C=2'
#inp = '(5+6)X3-13+L X0+(5-2X2)-#19+1L=2 CAROL 69'
#inp = 'EINSTEIN SUR VTELE (3+7)X3+1+1 1+L+C X#13+6X2=C X' #WORKS :D
        #EINSTEIN SUR VTELE (3+7)X3+1+1 1+L+C X#13+6X2=C X
#inp = '#19'
#inp = 'AVRIL LAVIGNE'
#inp = 'L L C6/3C X5/8/7-61-#35X8-C4-3X9C=2'

#inp = '#19+C7X#3C-1L+2 3+9+2X(7X#0)=2 dixie dixie dixi CHICKS !!!'
#inp = '(4-#8)X2+c I-3+L+2+0X(5+1X#13)X0=2 LIMA'
#inp = 'C+3X(1+2)-(#8+4)X3+7-2+L+C+I+0X(6+ X#18)1+1+2.'
#inp = '(2+#8)X2+3-2X I+L+#19+(7X2+3)+C+L=2+L+LOURAGAN SANDY LE DIX-HUITIEME CYCLONE'
#inp = '(2+4)X5+1 9-#18+L+C Ix(7+1x#3)+6=?MI7V I V UNIS ACTRICE L L I I' #11 nov 12
#inp = 'I I L L 4X5+16-#3+L+C I X(7+1X#18)+6=? MI37Y CYRUS ACTRICE'
#inp = 'I I L L 4X5+16-#3+L+ I (7+1#18)+6=? MI37Y CYRUS ACTRICE'
#inp = 'L L I I (4+ ?)X5+19-#8+L+I C ? (7+1 ? #10)+6=MI I C C 7Y CVRUS CHVNTEUSE'

#inp = '#17+C#4X#8C-L+2 8 +1 2+2X(7X#0)=2 ANGELINA' #Good
#inp = 'L L 5X C4+9+3C+4X C+3+8+2C+24:2=C' #good 20 novembre
#inp = '1 2 3 4 5 6 7 8 9 1 0 1 1.1 2 3 4 5 6 L 8 9 10 1 1. L EQUIPE DES FEMMES'
#inp = '1 7+9X2+3-(2+8)X2+L+C I-(6+9+#8)=C-' #Wrong 17 Nov should get 326
#inp = 'L L I I (4+?)X5+16-#3+L+C I ? (7+I ? #1)+6 = MI 37 Y CVRUS ACTICE' # 2012-11-16 2660
inp = '7+1+(7+1)X2+2-(7X0+1)+15-4X2+5 +7=VICTORIA BECKHAM' #16 decembre
#inp = raw_input()


#DIFFICULTY: Regular expression string splitting
items = findall('#([0-9]+)|([0-9]+)|([MDCLXVI]+)|([=-])', inp)
categories = zip(*items)

'''
testRomanToint = ['XCXCIVIV','IL','IC', 'VC', 'MIL', 'MDCXVI', 'CD', 'XC']
for test in testRomanToint:
    n = roman_to_int(test)
    print test, n, int_to_roman(n)
'''

som = [0]*4
arrVal = []
arrStrMatch = []
detailedInfo = []
catFunc = {0:digitalVal, 1:numbrVal, 2:romanVal, 3:otherVal}
for itemGroup in items:
    for i, item in enumerate(itemGroup):
        if item <> '':
            arrStrMatch.append(item)
            newArr = catFunc[i](item)
            som[i] += sum(newArr)
            arrVal += newArr
            
            dinfo = catFunc[i].__name__ +'\t'+item+'\t'
            if len(item)>1 or i==0:
                dinfo += '+'.join(substrings(item))+ '\t: '
                if i in (0,2): #Detail for Roman and digital nums
                    dinfo += '+'.join(map(str,newArr)) + '\t: '
            dinfo += str(sum(newArr))
            detailedInfo.append(dinfo)

#for items in categories:
#    print ' '.join([item for item in items if item <> ''])
print 'Input data :'
print inp
print 'Matched numbers :'
print ' '.join(arrStrMatch)
print 'Values :'
print '+'.join(map(str,arrVal))
print 'Sorted values :'
print '+'.join(map(str,[i for i in sorted(arrVal) if i > 0]))
print '\nDetailed category info :'
for i in catFunc:
    print catFunc[i].__name__, ':\t',' '.join([item for item in categories[i] if item <> '']), ':', som[i]

print '\nDetailed info :'
for dinfo in detailedInfo:
    print dinfo

print '\nResult :'
print sum(som)
