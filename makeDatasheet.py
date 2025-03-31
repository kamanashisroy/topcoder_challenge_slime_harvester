


BIOSLIME='BioSlime.py'
targets = []


for cleanupTurn in (700,750,800,850,900):
    for N in (10,12,14,16,18,20,22,24,26,28,30):
        for D in (1,2,4,6,8,10):
            for H in (1,2,4,6,8,10,12,14,16,18,20):
                targets.append( [f'N_{N}_D_{D}_H_{H}_{cleanupTurn}', [] ] )
                for S in [0.1]:#(0.1,0.3,0.5):
                    for P in [0.1,0.4]:#(0.1,0.3,0.5):
                            for W in [0.2]:
                                targets[-1][-1].append(f"java -jar tester.jar -exec 'python3 {BIOSLIME} -O --cleanupTurn={cleanupTurn} --noautocfg' -seed 100 -N {N} -D {D} -H {H} -delay 5 -S {S} -P {P} -W {W} -C 20 -novis >> $@")
                                #targets[-1][-1].append(f"python3 {BIOSLIME} -A -O --noautocfg --capacityMultipliyer={capacityMultipliyer} -N {N} -D {D} -H {H} -S {S} -P {P} -W {W} -C 20 >> $@")

ALL = [tgt for tgt,rules in targets]

#print('ALL='+' '.join(ALL))
print('all:'+' '.join(ALL))
print('')
print('clean:')
print('\trm -f N*')
print('')

for tgt,rules in targets:
    #print(tgt+':'+BIOSLIME)
    print(tgt+':')
    for r in rules:
        print('\t'+r)

