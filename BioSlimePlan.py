import sys
from heapq import heappop,heappush,heapify

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Read in N (grid size), C (max load capacity), and H (number of harvesters)
N = int(input())
C = int(input())
H = int(input())

# Read the location of each harvester
hr, hc, load = [], [], []
for h in range(H):
  row, col = input().split(" ")
  hr.append( int(row) )
  hc.append( int(col) )
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
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W': # or grid[nr][nc] == 'd':
                continue
            #eprint(r,c,'exploring ', nr,nc)
            if dist[nr][nc] is None or dist[nr][nc] >= (curdist+1):
                dist[nr][nc] = curdist+1
                source[nr][nc] = []
                heappush(hp,(curdist+1,nr,nc))
            if dist[nr][nc] >= (curdist+1):
                source[nr][nc].append((r,c))
    
    #eprint(r,c,'Done',dist)
    return [dist,source]        


# This path will be useful to return to depot
spath = dict()
for i,(r,c,tp) in enumerate(depots):
    if 'd' == tp:
        spath[i] = shortestPath(r,c)

def calcDir(distr,distc):
    for d in range(4):
        if distr == dr[d] and distc == dc[d]:
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

def hamiltondist(r1,c1,r2,c2):
    return abs(r2-r1)+abs(c2-c1)

def shortestPathAB(begr,begc,tgtr,tgtc,limit,explored):
    hp = [(hamiltondist(tgtr,tgtc,begr,begc),0,begr,begc)]
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

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W': #or grid[nr][nc] == 'd':
                continue
            if (nr,nc) not in dist or dist[(nr,nc)] >= (curdist+1):
                dist[(nr,nc)] = curdist+1
                source[(nr,nc)] = []
                heappush(hp,(hamiltondist(tgtr,tgtc,nr,nc),curdist+1,nr,nc))
            if dist[(nr,nc)] >= (curdist+1):
                source[(nr,nc)].append((r,c))
    
    return None



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

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W' or grid[nr][nc] == 'd':
                continue
            if (nr,nc) not in dist or dist[(nr,nc)] >= (curdist+1):
                dist[(nr,nc)] = curdist+1
                source[(nr,nc)] = []
                heappush(hp,(curdist+1,nr,nc))
            if dist[(nr,nc)] >= (curdist+1):
                source[(nr,nc)].append((r,c))
    
    return None

def moveToNearestDepot(r,c,explored, capacity):
    dist = []
    for i in range(len(depots)):
        dist.append( (spath[i][0][r][c], i) )
    unused,nearest = min(dist)

    # now find the path to nearest depot
    source = spath[nearest][1]
    #eprint(source,r,c,source[r][c])
    
    lr,lc = source[r][c][0]
    for lr,lc in source[r][c]:
        if (lr,lc) in explored or (capacity >= C and grid[lr][lc] == 's'):
            continue
        explored.remove((r,c))
        explored.add((lr,lc))
        return calcDir(lr-r,lc-c)
    return None

def moveAwayFromNearestDepot(r,c,explored, capacity):
    dist = []
    for i in range(len(depots)):
        dist.append( (spath[i][0][r][c], i) )
    unused,nearest = min(dist)

    dist = spath[nearest][0]
    for d in range(4):
        nr = hr[h] + dr[d]
        nc = hc[h] + dc[d]
        if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W': #or grid[nr][nc] == 'd':
            continue
        if (nr,nc) in explored:
            continue
        if dist[nr][nc] > dist[r][c]:
            explored.remove((r,c))
            explored.add((nr,nc))
            return calcDir(nr-r,nc-c)
    for d in range(4):
        nr = hr[h] + dr[d]
        nc = hc[h] + dc[d]
        if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W': #or grid[nr][nc] == 'd':
            continue
        if (nr,nc) in explored:
            continue
        if dist[nr][nc] == dist[r][c]:
            explored.remove((r,c))
            explored.add((nr,nc))
            return calcDir(nr-r,nc-c)
    return None

planPath = [None]*H

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
            slimes.append((r,c,grid[r][c]))
            # return to nearest depot ?
        elif grid[r][c] == 'W':# or grid[r][c] == 'd':
            explored.add((r,c))
            
    workersubgroups = dict()
    for h in range(H):
        r,c = hr[h],hc[h]
        explored.add((r,c))
        (subgrpr,subgrpc),(exr,exc) = calcSubGrid(r,c)
        if (subgrpr,subgrpc) not in workersubgroups:
            workersubgroups[(subgrpr,subgrpc)] = [h]
        else:
            workersubgroups[(subgrpr,subgrpc)].append(h)
        

    busysubgroups = set()
    moves = [None]*H

    for h in range(H):
        if moves[h] is not None:
            continue
        r,c = hr[h],hc[h]
        if load[h]>=C:
            # return to nearest depot ?
            moves[h] = moveToNearestDepot(r,c,explored,load[h])
            planPath[h] = None # reset plan
        else:
            if planPath[h] is not None:

                # get the plan
                (fr,cc),prev = planPath[h]
                if grid[fr][fc] != 's':
                    planPath[h] = None
                    continue

                if (r,c) not in prev:
                    planPath[h] = None
                    continue

                rr,cc = prev[(r,c)]
                if (rr,cc) in explored: # do not move
                    continue
                if (rr,cc) == (tgtr,tgtc):
                    planPath[h] = None # reset path

                explored.remove((r,c))
                explored.add((rr,cc))
                moves[h] = calcDir(rr-r,cc-c)

                (subgrpr,subgrpc),unused = calcSubGrid(r,c)
                busysubgroups.add((subgrpr,subgrpc))
 

    '''
    for sid,(sr,sc,unused) in enumerate(slimes):

        (subgrpr,subgrpc),(exr,exc) = calcSubGrid(sr,sc)

        if (subgrpr,subgrpc) in busysubgroups:
            continue
        # find available collecters in this group
        if (subgrpr,subgrpc) in workersubgroups:
            for h in workersubgroups[(subgrpr,subgrpc)]:
                if moves[h] is not None and planPath[h] is not None:
                    continue
                if load[h] < C: # we can use this worker
                    r,c = hr[h],hc[h]
                    #eprint(r,c,'Worker can collect slime',sr,sc)
                    planPath[h] = shortestPathAB(r,c,sr,sc,RN*RN,explored)
                    #tgtr,tgtc = shortestPathSubGrid(r,c,RN*RN,explored)
                    if planPath[h] is not None:
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
                    if moves[h] is not None and planPath[h] is not None:
                        continue
                    if load[h] < C: # we can use this worker
                        r,c = hr[h],hc[h]
                        #eprint(r,c,'Worker can collect slime',sr,sc)
                        planPath[h] = shortestPathAB(r,c,sr,sc,N*N,explored)
                        if planPath[h] is not None:
                            busysubgroups.add((subgrpr,subgrpc))
                            processed = True
                            break
            for newgrpr,newgrpc in [(subgrpr-1,subgrpc),(subgrpr-1,subgrpc-1),(subgrpr-1,subgrpc+1),(subgrpr+1,subgrpc),(subgrpr+1,subgrpc-1),(subgrpr+1,subgrpc+1),(subgrpr,subgrpc-1),(subgrpr,subgrpc+1)]:
                if newgrpr < 0 or newgrpc < 0 or newgrpr > RN or newgrpc > RN:
                    continue
                if (newgrpr,newgrpc) in exploredgrp:
                    continue
                stack.append((newgrpr,newgrpc))
                exploredgrp.add((newgrpr,newgrpc))
    '''

 
    for h in range(H):
        if moves[h] is not None:
            continue
        r,c = hr[h],hc[h]
        if load[h]>=C:
            # return to nearest depot ?
            
            moves[h] = moveToNearestDepot(r,c,explored,load[h])
            planPath[h] = None # reset plan
        else:

            if not planPath[h]:
                # get the subgrid
                (subgrpr,subgrpc),unused = calcSubGrid(r,c)
                if (subgrpr,subgrpc) in busysubgroups: # subgrid is busy
                    if load[h]:
                        moves[h] = moveToNearestDepot(r,c,explored,load[h])
                    else:
                        moves[h] = moveAwayFromNearestDepot(r,c,explored,load[h])
                else:
                    # find a slime in current subgrid
                    if len(slimes):
                        planPath[h] = shortestPathSubGrid(r,c,RN*RN,explored)
                    tgtr,tgtc = None,None
                    if planPath[h] is not None:
                        (fr,fc),prev = planPath[h]
                        tgtr,tgtc = prev[(r,c)]
                        if (fr,fc) == (tgtr,tgtc):
                            planPath[h] = None # reset path
                        if (tgtr,tgtc) in explored: # do not move
                            continue

                    if tgtr is not None and (tgtr,tgtc) not in explored:
                        busysubgroups.add((subgrpr,subgrpc))
                        explored.remove((r,c))
                        explored.add((tgtr,tgtc))
                        moves[h] = calcDir(tgtr-r,tgtc-c)
                        #eprint('moving to ',tgtr,tgtc, explored)
                    elif load[h]: # move the load to nearest depot
                        moves[h] = moveToNearestDepot(r,c,explored,load[h])
                        planPath[h] = None
                    else: # move away from nearest depot
                        moves[h] = moveAwayFromNearestDepot(r,c,explored,load[h])
                        planPath[h] = None
            else:
                #eprint(planPath[h])
                (fr,fc),prev = planPath[h]
                if grid[fr][fc] != 's':
                    planPath[h] = None
                    continue
                tgtr,tgtc = prev[(r,c)]
                if (tgtr,tgtc) in explored: # do not move
                    continue
                if (fr,fc) == (tgtr,tgtc):
                    planPath[h] = None # reset path
                explored.remove((r,c))
                explored.add((tgtr,tgtc))
                moves[h] = calcDir(tgtr-r,tgtc-c)


    cmd = ""
    # Move each harvester
    for h in range(H):
        if moves[h] is not None:
            d = moves[h]
            cmd += f"{h} {dname[d]} "
            nr = hr[h] + dr[d]
            nc = hc[h] + dc[d]
            if grid[nr][nc] != 'd':
                hr[h] = nr
                hc[h] = nc
            #explored.add((nr,nc))
            assert(not( nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W'))
        else:
            cmd += f"{h} X "

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

