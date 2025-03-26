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
                    return rr,cc
                if rr == begr and cc == begc:
                    continue
                for pr,pc in source[(rr,cc)]:
                    if (dist[(pr,pc)] + cost + 1) > curdist:
                        continue
                    stack.append( (cost+1,pr,pc))
            #eprint(begr,begc,'No steps to take!')
            #return None,None
        if curdist > limit:
           return None,None

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if nc<0 or nc>=N or nr<0 or nr>=N or grid[nr][nc]=='W': #or grid[nr][nc] == 'd':
                continue
            if (nr,nc) not in dist or dist[(nr,nc)] >= (curdist+1):
                dist[(nr,nc)] = curdist+1
                source[(nr,nc)] = []
                heappush(hp,(curdist+1,nr,nc))
            if dist[(nr,nc)] >= (curdist+1):
                source[(nr,nc)].append((r,c))
    
    return None,None

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
            
    for h in range(H):
        r,c = hr[h],hc[h]
        explored.add((r,c))

    subgrids = set()
    moves = [None]*H
    
    for h in range(H):
        r,c = hr[h],hc[h]
        if load[h]>=C:
            # return to nearest depot ?
            
            moves[h] = moveToNearestDepot(r,c,explored,load[h])
        else:

            # get the subgrid
            (rr,cc),unused = calcSubGrid(r,c)
            if (rr,cc) in subgrids: # subgrid is busy
                if load[h]:
                    moves[h] = moveToNearestDepot(r,c,explored,load[h])
                else:
                    moves[h] = moveAwayFromNearestDepot(r,c,explored,load[h])
            else:
                # find a slime in current subgrid
                tgtr,tgtc = None,None
                if len(slimes):
                    tgtr,tgtc = shortestPathSubGrid(r,c,RN*RN,explored)
                subgrids.add((rr,cc))
                if tgtr is not None and (tgtr,tgtc) not in explored:
                    explored.remove((r,c))
                    explored.add((tgtr,tgtc))
                    moves[h] = calcDir(tgtr-r,tgtc-c)
                elif load[h]: # move the load to nearest depot
                    moves[h] = moveToNearestDepot(r,c,explored,load[h])
                else: # move away from nearest depot
                    moves[h] = moveAwayFromNearestDepot(r,c,explored,load[h])

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

