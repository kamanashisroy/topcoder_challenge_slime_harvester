


BIOSLIME='BioSlime.py'
targets = []

for N in range(10,20): #range(10,31):
    for D in range(1,5): #range(1,11):
        for H in range(8,16):#range(1,21):
            targets.append( ['N_{N}_D_{D}_H_{H}_NOPARAM'.format(N=N,D=D,H=H), [] ] )
            for S in [0.1]:#(0.1,0.3,0.5):
                for P in [0.1]:#(0.1,0.3,0.5):
                    for W in [0.1,0.2]:
                        targets[-1][-1].append("java -jar tester.jar -exec 'python3 {BIOSLIME}' -seed 100 -N {N} -D {D} -H {H} -delay 5 -S {S} -P {P} -W {W} -novis >> $@".format(N=N,D=D,H=H,S=S,P=P,W=W,BIOSLIME=BIOSLIME))

ALL = [tgt for tgt,rules in targets]

#print('ALL='+' '.join(ALL))
print('all:'+' '.join(ALL))
print('')
print('clean:')
print('\trm -f N*')
print('')

for tgt,rules in targets:
    print(tgt+':'+BIOSLIME)
    for r in rules:
        print('\t'+r)

