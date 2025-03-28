import os
import re


pat = r'..N_(?P<N>\d*)_D_(?P<D>\d*)_H_(?P<H>\d*)_(?P<aa>\d)'
p = re.compile(pat)
table = dict()
def parseFile(filename):
    # ./N_19_D_1_H_8_0.1.2.3.0.1.2.3
    m = p.match(filename)
    N,D,H = int(m.group('N')),int(m.group('D')),int(m.group('H'))
    key = (N,D,H)
    scores = []
    print('opening',filename,key)
    with open(filename) as fd:
        for line in fd:
            scores.append(float(line[8:]))
    if scores:
        if key not in table:
            table[key] = []

        table[key].append([m.group('aa'),scores])
    

folder_path = '.'

files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

#print(files)
for f in files:
    if f[:3] == './N':
        parseFile(f)

print(table)
print(table.keys())
result = [None]*31
for N in range(10,31):
    result[N] = [None]*11
    for D in range(1,11):
        result[N][D] = [None]*21
        for H in range(1,21):
            bestscore = None
            bestparam = None

            if (N,D,H) in table:
                print('collecting',table[(N,D,H)])
                for param,scores in table[(N,D,H)]:
                    avscore = sum(scores)/len(scores)
                    if bestscore is None or bestscore < avscore:
                        bestscore = avscore
                        bestparam = param
            result[N][D][H] = int(bestparam)

print(result)
