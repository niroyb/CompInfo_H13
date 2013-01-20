from re import findall
from itertools import product, combinations
import sys

def substrings(string):
    return [string[s:e] for s,e in combinations(xrange(len(string)+1), 2)]

#http://code.activestate.com/recipes/81611-roman-numerals/
numeral_map = zip((1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'))

def int_to_roman(i): #DIFFICULTY: Correct implementation
    result = []
    for integer, numeral in numeral_map:
        count = int(i / integer)
        result.append(numeral * count)
        i -= integer * count
    return ''.join(result)

def roman_to_int(n): #DIFFICULTY: Correct implementation with error checking
    n = unicode(n).upper()
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result if n == int_to_roman(result) else 0 #DANGER: Return value only if valid roman numeral

def digitalVal(item):
    som = 0
    dico = {'0':('0','1','7'), '1':('1'), '2':('2'), '3':('1','3','7'), '4':('1','4'), '5':('5'),'6':('5','6'),
            '7':('1','7'), '8':('0','1','2','3','4','5','6','7','8','9'), '9':('1','3','4','5','7','9')}
    for subStr in substrings(item):
        lists = [dico[n] for n in subStr]
        #DIFFICULTY: Arbitrarly sized cartesian product, #DANGER: Do not count combinations starting with 0
        som += sum(map(int, [i for i in [''.join(c) for c in product(*lists)] if i[0] <> '0']))
    return som

def numbrVal(item): return sum([int(i) for i in substrings(item) if i[0] <> '0']) #DANGER: Do not count combinations starting with 0
def romanVal(item): return sum(map(roman_to_int, substrings(item)))
def otherVal(item): return {'-':1, '=':4}[item]

items = findall('#([0-9]+)|([0-9]+)|([MDCLXVI]+)|([=-])', raw_input()) #DIFFICULTY: Reg-Ex for splitting the string in groups
categories = zip(*items)
som = 0
catFunc = {0:digitalVal, 1:numbrVal, 2:romanVal, 3:otherVal}
for i, category in enumerate(categories):
    for item in category:
        if item <> '':
            som += catFunc[i](item) #Smells like bad code :)
sys.stdout.write(str(som))
