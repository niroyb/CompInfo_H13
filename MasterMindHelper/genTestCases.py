import mastermindSolve

def genTestCases():
    cases = ['4664 02\n4664 03',
                '4664 02\n4351 03',
                '1234 03\n2342 12',
                '4664 02\n5145 02',
                '3232 00\n5644 00',
                '5353 02\n4645 02\n1434 01',
                '2566 10\n1534 02\n2411 20\n2423 21',
                '2654 10\n2233 10',
                '4635 02',
                '6523 12\n1532 20\n4536 11\n2562 11\n6632 40',
                '6521 11\n5532 00\n1641 12',
                '5361 12\n1564 11',
                '6362 01\n1254 02\n4163 12\n2556 01\n5135 01',
                '2326 01\n3662 01\n1334 02\n4665 02\n1315 02\n5623 20',
                '2566 10\n1534 02\n2411 20\n2423 23',
                '2566 10\n1534 02\n2411 20\n2423 03']
    for i, inp in enumerate(cases):
        with open('test_in_'+str(i)+'.txt', 'w') as f:
            f.write(inp)
        with open('test_out_'+str(i)+'.txt', 'w') as f:
            f.write(mastermindSolve.getSolutionMasterMind(inp))

genTestCases()
