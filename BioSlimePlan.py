import sys
from heapq import heappop,heappush,heapify

debug = False
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Read in N (grid size), C (max load capacity), and H (number of harvesters)
N = int(input())
C = int(input())
H = int(input())

# Read the location of each harvester
har, load = [], []
for h in range(H):
  row, col = input().split(" ")
  har.append( [int(row),int(col)] )
  load.append(0)

grid = [[' ' for x in range(N)] for y in range(N)]
# Read the starting grid configuration
for r in range(N):
  for c in range(N):
    grid[r][c] = input()

depots = []
depotId = dict()
for r in range(N):
  for c in range(N):
    if grid[r][c] == 'd':
        depotId[(r,c)] = len(depots)
        depots.append((r,c,grid[r][c]))

# Define movement directions (right, down, left, up)
dc = [1,0,-1,0]
dr = [0,1,0,-1]
dname = ['R','D','L','U']

def iterMoves(r,c):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W' or grid[nr][nc] == 'd':
            continue
        yield (nr,nc)
    
def iterMovesGivenExplored(r,c,explored,capacity):
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W' or grid[nr][nc] == 'd':
            continue
        if (nr,nc) in explored or (capacity >= C and grid[nr][nc] == 's'):
            continue
        yield (nr,nc)
 
# At first find the shortest path 
def shortestPath(begr,begc):
    hp = [(0,begr,begc)]
    dist = [[None]*N for _ in range(N)]
    source = [[None]*N for _ in range(N)]
    dist[begr][begc] = 0

    while hp:
        curdist, r, c = heappop(hp)
        if curdist > dist[r][c]:
            continue
        for nr,nc in iterMoves(r,c):
            #eprint(r,c,'exploring ', nr,nc)
            if dist[nr][nc] is None or dist[nr][nc] > (curdist+1):
                dist[nr][nc] = curdist+1
                source[nr][nc] = []
                heappush(hp,(curdist+1,nr,nc))
            if dist[nr][nc] >= (curdist+1):
                source[nr][nc].append((r,c))
    
    #eprint(r,c,'Done',dist)
    return [dist,source]        


# This path will be useful to return to depot
shortestPathFromDepot = dict()
for i,(r,c,tp) in enumerate(depots):
    if 'd' == tp:
        shortestPathFromDepot[i] = shortestPath(r,c)

#eprint(shortestPathFromDepot)

def calcDir(nr,nc,r,c):
    distr = nr-r
    distc = nc-c
    for d in range(4):
        if distr == dr[d] and distc == dc[d]:
            assertPath(d,nr,nc,r,c)
            return d

# split the grid into small parts
# total cells = N*N
# we can make subgrid of size root(N)*root(N)

RN = 1
while (RN*RN) < N:
    RN += 1

       

def calcSubGrid(r,c):
    subr,r2 = divmod(r,RN)
    subc,c2 = divmod(c,RN)
    return (subr,subc),(r2,c2)

def mahattandist(r1,c1,r2,c2):
    return abs(r2-r1)+abs(c2-c1)

def buildHarvestorSubGrids():
    subgrids = dict()
    for h,(r,c) in enumerate(har):
        subgrp,unused = calcSubGrid(r,c)
        if subgrp not in subgrids:
            subgrids[subgrp] = [h]
        else:
            subgrids[subgrp].append(h)
    return subgrids

def buildSlimeSubGrids(slimes):
    subgrids = dict()
    for i,(r,c) in enumerate(slimes):
        subgrp,unused = calcSubGrid(r,c)
        if subgrp not in subgrids:
            subgrids[subgrp] = [i]
        else:
            subgrids[subgrp].append(i)
    return subgrids



garrages = [None]*H
harvgrids = buildHarvestorSubGrids()
# Make a resting point for all the harvesters
for r in range(N):
    for c in range(N):
        if c<0 or c>=N or r<0 or r>=N or grid[r][c]=='W' or grid[r][c] == 'd':
            continue
        for g in garrages:
            if g is not None and mahattandist(g[0],g[1],r,c) < 10:
                break
        else:
            subgrp,unused = calcSubGrid(r,c)
            if subgrp in harvgrids:
                for h in harvgrids[subgrp]:
                    if garrages[h] is None:
                        garrages[h] = (r,c)
                        break
        
# This path will be useful to return to depot
shortestPathFromGarrages = [None]*H
for i,g in enumerate(garrages):
    if g is not None:
        shortestPathFromGarrages[i] = shortestPath(g[0],g[1])
        

def shortestPathAB(begr,begc,tgtr,tgtc,limit,explored):
    hp = [(mahattandist(tgtr,tgtc,begr,begc),0,begr,begc)]
    dist = dict()
    source = dict()
    dist[(begr,begc)] = 0

    while hp:
        ham,curdist, r, c = heappop(hp)
        if curdist > dist[(r,c)]:
            continue
        if grid[r][c] == 's' and (begr,begc) != (r,c):

            prev = dict()
            #eprint(begr,begc,'found s',r,c)
            stack = [(0,r,c)]
            while stack:
                #eprint(stack)
                cost,rr,cc = stack.pop()
                if dist[(rr,cc)] == 1:
                    if (rr,cc) in explored :
                        #eprint(rr,cc,'already explored')
                        continue
                    #eprint(begr,begc,'Should move to ',rr,cc,'to collect', r,c,'dist',curdist)
                    prev[(begr,begc)] = (rr,cc)
                    return (r,c),prev
                if rr == begr and cc == begc:
                    continue
                for pr,pc in source[(rr,cc)]:
                    if (dist[(pr,pc)] + cost + 1) > curdist:
                        continue
                    stack.append( (cost+1,pr,pc))
                    prev[(pr,pc)] = (rr,cc)
            #eprint(begr,begc,'No steps to take!')
            #return None,None
        if curdist > limit:
           return None

        for nr,nc in iterMoves(r,c):
            if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                dist[(nr,nc)] = curdist+1
                source[(nr,nc)] = []
                heappush(hp,(mahattandist(tgtr,tgtc,nr,nc),curdist+1,nr,nc))
            if dist[(nr,nc)] >= (curdist+1):
                source[(nr,nc)].append((r,c))
    
    return None

def assertPath(d,nr,nc,r,c):
    nr2 = r + dr[d]
    nc2 = c + dc[d]
    assert(nr == nr2)
    assert(nc == nc2)
    return d
    

def shortestPathSubGrid(begr,begc,limit,explored):
    hp = [(0,begr,begc)]
    dist = dict()
    source = dict()
    dist[(begr,begc)] = 0

    while hp:
        curdist, r, c = heappop(hp)
        if curdist > dist[(r,c)]:
            continue
        if grid[r][c] == 's' and (begr,begc) != (r,c):

            prev = dict()
            #eprint(begr,begc,'found s',r,c)
            stack = [(0,r,c)]
            while stack:
                #eprint(stack)
                cost,rr,cc = stack.pop()
                if dist[(rr,cc)] == 1:
                    if (rr,cc) in explored :
                        #eprint(rr,cc,'already explored')
                        continue
                    #eprint(begr,begc,'Should move to ',rr,cc,'to collect', r,c,'dist',curdist)
                    #grid[r][c] = '.' # do not allow others find it
                    prev[(begr,begc)] = (rr,cc)
                    return [(r,c),prev]
                if rr == begr and cc == begc:
                    continue
                for pr,pc in source[(rr,cc)]:
                    if (dist[(pr,pc)] + cost + 1) > curdist:
                        continue
                    stack.append( (cost+1,pr,pc))
                    prev[(pr,pc)] = (rr,cc)
            #eprint(begr,begc,'No steps to take!')
            #return None,None
        if curdist > limit:
           return None

        for nr,nc in iterMoves(r,c):
            if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                dist[(nr,nc)] = curdist+1
                source[(nr,nc)] = []
                heappush(hp,(curdist+1,nr,nc))
            if dist[(nr,nc)] >= (curdist+1):
                source[(nr,nc)].append((r,c))
    
    return None

def followPath(r,c,path,explored,capacity):
    (fr,fc),prev = path
    if grid[fr][fc] != 's':
        return None

    if (r,c) not in prev:
        return None
    nr,nc = prev[(r,c)]
    if (nr,nc) in explored:
        return None # cannot follow path
    if grid[nr][nc] == 's' and capacity >= C:
        return None # cannot follow path
    assert((r,c) in explored)
    if grid[nr][nc] != 'd':
        #explored.remove((r,c))
        explored.add((nr,nc))
    return calcDir(nr,nc,r,c)

def moveToNearestDepot(r,c,explored, capacity, depotbusy):
    dist = []
    for i in range(len(depots)):
        if depotbusy[i]:
            continue
        if shortestPathFromDepot[i][0][r][c] is not None:
            dist.append( (shortestPathFromDepot[i][0][r][c], i) )
    if not dist:
        return None
    #eprint(r,c,'move to neareest', dist, depotbusy)
    unused,nearest = min(dist)

    # now find the path to nearest depot
    source = shortestPathFromDepot[nearest][1]
    #eprint(source,r,c,source[r][c])
    if not source[r][c]:
        # FIXME probably we entered into the depot
        #return None
        return moveAwayFromNearestDepot(r,c,explored,capacity,depotbusy)
    
    lr,lc = source[r][c][0]
    for lr,lc in source[r][c]:
        if (lr,lc) in explored or (capacity >= C and grid[lr][lc] == 's'):
            continue
        assert((r,c) in explored)
        if grid[lr][lc] != 'd':
            #explored.remove((r,c))
            explored.add((lr,lc))
        depotbusy[nearest] = True 
        return calcDir(lr,lc,r,c)
    #return moveAwayFromNearestDepot(r,c,explored,capacity)
    return None

def moveAwayFromNearestDepot(r,c,explored, capacity, depotbusy):
    dist = []
    for i in range(len(depots)):
        #if depotbusy[i]:
        #    continue
        if shortestPathFromDepot[i][0][r][c] is not None:
            dist.append( (shortestPathFromDepot[i][0][r][c], i) )
    unused,nearest = min(dist)

    dist = shortestPathFromDepot[nearest][0]
    if dist[r][c] is None: # we entered into a depot
        for nr,nc in iterMovesGivenExplored(r,c, explored, capacity):
            explored.add((nr,nc))
            return calcDir(nr,nc,r,c)
        return None
        
    for nr,nc in iterMovesGivenExplored(r,c, explored, capacity):
        if dist[nr][nc] is None: # do not enter into a depot
            continue
        if dist[nr][nc] > dist[r][c]:
            assert((r,c) in explored)
            if grid[nr][nc] != 'd':
                #explored.remove((r,c))
                explored.add((nr,nc))
            return calcDir(nr,nc,r,c)
    for nr,nc in iterMovesGivenExplored(r,c, explored, capacity):
        if dist[nr][nc] is None: # do not enter into a depot
            continue
        if dist[nr][nc] >= dist[r][c]: # get away even if there is wiggle room
            assert((r,c) in explored)
            if grid[nr][nc] != 'd':
                #explored.remove((r,c))
                explored.add((nr,nc))
            return calcDir(nr,nc,r,c)

    return None


def moveToNearestGarrage(r,c,explored, capacity):
    for i,(rr,cc) in enumerate(har):
        if (rr,cc) == (r,c):
            nearest = i
            break
    else:
        return None
    if shortestPathFromGarrages[nearest] is None:
        return None
    '''
    dist = []
    for i in range(H):
        if shortestPathFromGarrages[i] is not None and shortestPathFromGarrages[i][0][r][c] is not None:
            dist.append( (shortestPathFromGarrages[i][0][r][c], i) )
    if not dist:
        return None
    #eprint(r,c,'move to neareest', dist, depotbusy)
    unused,nearest = min(dist)
    '''

    # now find the path to nearest depot
    source = shortestPathFromGarrages[nearest][1]
    #eprint(source,r,c,source[r][c])
    if not source[r][c]:
        # FIXME probably we entered into the garrage
        return None
    
    lr,lc = source[r][c][0]
    for lr,lc in source[r][c]:
        if (lr,lc) in explored or (capacity >= C and grid[lr][lc] == 's'):
            continue
        assert((r,c) in explored)
        if grid[lr][lc] != 'd':
            #explored.remove((r,c))
            explored.add((lr,lc))
        return calcDir(lr,lc,r,c)
    return None


planPath = [None]*H
collide = [False]*H
depotbad = [False]*len(depots)

# Simulate 1000 turns
for turn in range(0,1000):

    explored = set()

    # find the slimes and nearest harvestors
    slimes = []
    slimeId = dict()
    for r in range(N):
      for c in range(N):
        if grid[r][c] == 's':
            slimeId[(r,c)] = len(slimes)
            slimes.append((r,c))
            # return to nearest depot ?
        elif grid[r][c] == 'W':# or grid[r][c] == 'd':
            explored.add((r,c))
            

    busysubgroups = set()
    moveCmds = [None]*H

    for h,(r,c) in enumerate(har):
        if collide[h] is not None and grid[r][c] != 'H':
            cr,cc = collide[h]
            moveCmds[h] = calcDir(r,c,cr,cc)
            for i,(dr,dc) in enumerate(depots):
                if (dr,dc) == (cr,cc):
                    depotbad[i] = True
                    break
            har[h] = [cr,cc]
            collide[h] = None
    depotbusy = depotbad[:]

    for h,(r,c) in enumerate(har):
        explored.add((r,c))

    for h,(r,c) in enumerate(har):
        if moveCmds[h] is not None:
            continue
        subgrp,unused = calcSubGrid(r,c)
        if load[h]>=C:
            planPath[h] = None # reset plan
            moveCmds[h] = moveToNearestDepot(r,c,explored,load[h],depotbusy)
            if moveCmds[h] is not None:
                busysubgroups.add(subgrp)
            else:
                #moveCmds[h] = moveToNearestGarrage(r,c,explored, load[h])
                pass
        else:
            if planPath[h] is not None:

                # get the plan
                moveCmds[h] = followPath(r,c,planPath[h],explored,load[h])
                if moveCmds[h] is None:
                    planPath[h] = None
                    if load[h]: # move the load to nearest depot
                        moveCmds[h] = moveToNearestDepot(r,c,explored,load[h],depotbusy)
                        if moveCmds[h] is not None:
                            busysubgroups.add(subgrp)
                    else: # move away from nearest depot
                        #moveCmds[h] = moveAwayFromNearestDepot(r,c,explored,load[h],depotbusy)
                        moveCmds[h] = moveToNearestGarrage(r,c,explored, load[h])
                else:
                    busysubgroups.add(subgrp)
 

    slimeSubGrids = buildSlimeSubGrids(slimes)
    '''
    workersubgroups = buildHarvestorSubGrids()
    for sid,(sr,sc,unused) in enumerate(slimes):

        (subgrpr,subgrpc),(exr,exc) = calcSubGrid(sr,sc)

        if (subgrpr,subgrpc) in busysubgroups:
            continue
        # find available collecters in this group
        if (subgrpr,subgrpc) in workersubgroups:
            for h in workersubgroups[(subgrpr,subgrpc)]:
                if moveCmds[h] is not None or planPath[h] is not None:
                    continue
                if load[h] < C: # we can use this worker
                    r,c = hr[h],hc[h]
                    #eprint(r,c,'Worker can collect slime',sr,sc)
                    planPath[h] = shortestPathAB(r,c,sr,sc,RN*RN,explored)
                    #tgtr,tgtc = shortestPathSubGrid(r,c,RN*RN,explored)
                    if planPath[h] is not None:
                        moveCmds[h] = followPath(r,c,planPath[h],explored,load[h])
                        if moveCmds[h] is None:
                            planPath[h] = None
                        else:
                            busysubgroups.add((subgrpr,subgrpc))
                            break
    
    for sid,(sr,sc,unused) in enumerate(slimes):

        (curgrpr,curgrpc),(exr,exc) = calcSubGrid(sr,sc)
        if (curgrpr,curgrpc) in busysubgroups:
            continue
        exploredgrp = set()
        stack = [(curgrpr,curgrpc)]
        exploredgrp.add((curgrpr,curgrpc))

        processed = False
        while stack and not processed:
            subgrpr,subgrpc = stack.pop()
            
            if (subgrpr,subgrpc) in workersubgroups and (subgrpr,subgrpc) not in busysubgroups:
                for h in workersubgroups[(subgrpr,subgrpc)]:
                    if moveCmds[h] is not None or planPath[h] is not None:
                        continue
                    if load[h] < C: # we can use this worker
                        r,c = hr[h],hc[h]
                        #eprint(r,c,'Worker can collect slime',sr,sc)
                        planPath[h] = shortestPathAB(r,c,sr,sc,N*N,explored)
                        if planPath[h] is not None:
                            moveCmds[h] = followPath(r,c,planPath[h],explored,load[h])
                            if moveCmds[h] is None:
                                planPath[h] = None
                            else:
                                busysubgroups.add((subgrpr,subgrpc))
                                break
            for newgrpr,newgrpc in [(subgrpr-1,subgrpc),(subgrpr-1,subgrpc-1),(subgrpr-1,subgrpc+1),(subgrpr+1,subgrpc),(subgrpr+1,subgrpc-1),(subgrpr+1,subgrpc+1),(subgrpr,subgrpc-1),(subgrpr,subgrpc+1)]:
                if newgrpr < 0 or newgrpc < 0 or newgrpr > RN or newgrpc > RN:
                    continue
                if (newgrpr,newgrpc) in exploredgrp:
                    continue
                stack.append((newgrpr,newgrpc))
                exploredgrp.add((newgrpr,newgrpc))
    '''

 
    for h,(r,c) in enumerate(har):
        if moveCmds[h] is not None:
            continue
        subgrp,unused = calcSubGrid(r,c)
        if load[h]>=C:
            planPath[h] = None # reset plan
            # return to nearest depot ?
            if subgrp in busysubgroups:
                moveCmds[h] = moveAwayFromNearestDepot(r,c,explored,load[h],depotbusy)
            else:
                moveCmds[h] = moveToNearestDepot(r,c,explored,load[h],depotbusy)
                busysubgroups.add(subgrp)
        else:

            if not planPath[h]:
                # get the subgrid
                if subgrp in busysubgroups: # subgrid is busy
                    #if load[h]:
                    #    moveCmds[h] = moveToNearestDepot(r,c,explored,load[h],depotbusy)
                    #else:
                    #moveCmds[h] = moveAwayFromNearestDepot(r,c,explored,load[h],depotbusy)
                    moveCmds[h] = moveToNearestGarrage(r,c,explored,load[h])
                else:
                    # find a slime in current subgrid
                    if subgrp in slimeSubGrids and slimeSubGrids[subgrp]:
                        planPath[h] = shortestPathSubGrid(r,c,RN*RN,explored)
                    if planPath[h] is None and slimes and (turn%20 == 0):
                        planPath[h] = shortestPathSubGrid(r,c,RN*RN,explored)
                    if planPath[h] is not None:
                        moveCmds[h] = followPath(r,c,planPath[h],explored,load[h])
                    if moveCmds[h] is None:
                        planPath[h] = None
                        #eprint('moving to ',tgtr,tgtc, explored)
                        if load[h]: # move the load to nearest depot
                            moveCmds[h] = moveToNearestDepot(r,c,explored,load[h],depotbusy)
                            if moveCmds[h] is not None:
                                busysubgroups.add(subgrp)
                        else: # move away from nearest depot
                            moveCmds[h] = moveAwayFromNearestDepot(r,c,explored,load[h],depotbusy)
                    else:
                        busysubgroups.add(subgrp)
            else:
                moveCmds[h] = followPath(r,c,planPath[h],explored,load[h])
                if moveCmds[h] is None:
                    planPath[h] = None
                    moveCmds[h] = moveAwayFromNearestDepot(r,c,explored,load[h],depotbusy)
                else:
                    busysubgroups.add(subgrp)

    if debug:
        eprint('============================================')
    harvpos = set()
    cmd = ""
    # Move each harvester
    for h,(r,c) in enumerate(har):
        if moveCmds[h] is not None:
            d = moveCmds[h]
            cmd += f"{h} {dname[d]} "

            if debug:
                # debug begins
                curgrid = grid[r][:]
                eprint(curgrid,r,c)
                curgrid[c] = '!'
                eprint(curgrid,r,c)
                # debug ends

            nr = r + dr[d]
            nc = c + dc[d]
            if grid[nr][nc] == 'd':
                planPath[h] = None
                collide[h]  = (nr,nc)
            else:
                har[h] = [nr,nc]
            
            rr,cc = har[h]
            #explored.add((nr,nc))
            if debug:
                # debug begins
                curgrid = grid[rr][:]
                eprint(curgrid,'A',rr,cc)
                curgrid[cc] = '!'
                eprint(curgrid,'A',rr,c)
                # debug ends

            if debug:
                assert((rr,cc) not in harvpos)
                harvpos.add((rr,cc))
                assert(not( nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W'))
        else:
            cmd += f"{h} X "
            if debug:
                #assert((rr,cc) not in harvpos)
                harvpos.add((rr,cc))

    if debug:
        sys.stderr.flush()

    # Output the command for the turn
    print(cmd)
    sys.stdout.flush()

    # Read the elapsed time
    tm = int(input())
    load = []

    # Read the number of fuel carried by each harvester
    for h in range(H):
        load.append(int(input()))

    # Read the updated grid
    for r in range(N):
        for c in range(N):
            grid[r][c] = input()

