import os
import re

# N_15_D_3_H_8_7_13
pat = r'..N_(?P<N>\d*)_D_(?P<D>\d*)_H_(?P<H>\d*)_C_(?P<C>\d*)_(?P<cleanupTurn>\d*)'
p = re.compile(pat)
table = dict()
def parseFile(filename):
    # ./N_19_D_1_H_8_0.1.2.3.0.1.2.3
    m = p.match(filename)
    N,D,H,C = int(m.group('N')),int(m.group('D')),int(m.group('H')),int(m.group('C'))
    key = (N,D,H,C)
    scores = []
    print('opening',filename,key)
    with open(filename) as fd:
        for line in fd:
            if line.startswith('Score = '):
                scores.append(float(line[8:]))
    if scores:
        if key not in table:
            table[key] = []

        table[key].append([int(m.group('cleanupTurn')),scores])
    

folder_path = '.'

files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

#print(files)
for f in files:
    if f[:3] == './N':
        parseFile(f)

#print(table)
#print(table.keys())
result = [None]*31
for N in range(10,31):
    result[N] = [None]*11
    hasNval = False
    for D in range(1,11):
        hasDval = False
        result[N][D] = [None]*21
        for H in range(1,21):
            result[N][D][H] = [None]*11
            hasHval = False
            for C in range(11):
                bestscore = None
                bestparam = None

                if (N,D,H,C) in table:
                    #print('collecting',table[(N,D,H)])
                    for param,scores in table[(N,D,H,C)]:
                        avscore = sum(scores)/len(scores)
                        if bestscore is None or bestscore < avscore:
                            bestscore = avscore
                            bestparam = param
                    hasHval = True
                    hasDval = True
                    hasNval = True
                    result[N][D][H][C] = bestparam
            if not hasHval:
                result[N][D][H] = None
        if not hasDval:
            result[N][D] = None
    if not hasNval:
        result[N] = None
print(result)
