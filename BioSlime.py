
import time
import sys
from heapq import heappop,heappush,heapify

debug = False
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


class BioSlime:
    def __init__(self,tester):
        self.tester = tester
        self.N = tester.N
        self.C = tester.C
        self.H = tester.H
        self.grid = [[' ' for x in range(self.N)] for y in range(self.N)]

        # Define movement directions (right, down, left, up)
        self.dc = [1,0,-1,0]
        self.dr = [0,1,0,-1]
        self.harstr = [str(x) for x in range(self.H)]

        self.RN = 1
        while (self.RN*self.RN) < self.N:
            self.RN += 1

        self.planPath = [None]*self.H


    def setup(self):
        # Read the location of each harvester
        self.load = [0]*self.H
        self.har = self.tester.setupHarvester()

        self.tester.parseGrid(self.grid)

        self.depots = []
        self.depotId = dict()
        for r in range(self.N):
          for c in range(self.N):
            if self.grid[r][c] == 'd':
                self.depotId[(r,c)] = len(self.depots)
                self.depots.append((r,c))
        self.D = len(self.depots)
        self.depotbad = [False]*self.D

        # This path will be useful to return to depot
        self.buildShortestPathFromDepot()
        self.buildGarrages()

    def buildShortestPathFromDepot(self):
        self.shortestPathFromDepot = [None]*self.D
        for i,(r,c) in enumerate(self.depots):
            if not self.depotbad[i]:
                self.shortestPathFromDepot[i] = self.shortestPath(r,c)


    def buildGarrages(self):
        self.garrages = [None]*self.H
        numGarrages = 0
        #harvgrids = self.buildHarvestorSubGrids()
        self.shortestPathFromGarrages = [None]*self.H
        # Make a resting point for all the harvesters
        for r in range(self.N):
            for c in range(self.N):
                if numGarrages == self.H:
                    return
                if c<0 or c>=self.N or r<0 or r>=self.N or self.grid[r][c]=='W' or self.grid[r][c] == 'd':
                    continue
                for g in self.garrages:
                    if g is not None and self.manhatdist(g[0],g[1],r,c) < 10:
                        break
                else:

                    gidx = None
                    for h in range(self.H):
                        if self.garrages[h] is not None:
                            continue
                        if gidx is None:
                            gidx = h
                        else:
                            hr,hc = self.har[h]
                            gr,gc = self.har[gidx]
                            if self.manhatdist(hr,hc,r,c) < self.manhatdist(gr,gc,r,c):
                                gidx = h

                    if gidx is not None:
                        self.garrages[gidx] = (r,c)
                        self.shortestPathFromGarrages[gidx] = self.shortestPath(r,c)
                        numGarrages += 1
                    

    def assertPath(self,d,nr,nc,r,c):
        nr2 = r + self.dr[d]
        nc2 = c + self.dc[d]
        assert(nr == nr2)
        assert(nc == nc2)
        return d
 
    def calcDir(self,nr,nc,r,c):
        distr = nr-r
        distc = nc-c
        for d in range(4):
            if distr == self.dr[d] and distc == self.dc[d]:
                self.assertPath(d,nr,nc,r,c)
                return d

    def iterMoves(self,r,c):
        for d in range(4):
            nr = r + self.dr[d]
            nc = c + self.dc[d]
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W' or self.grid[nr][nc] == 'd':
                continue
            yield (nr,nc)
        
    def iterMovesGivenExplored(self,r,c,explored,myload):
        for d in range(4):
            nr = r + self.dr[d]
            nc = c + self.dc[d]
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W' or self.grid[nr][nc] == 'd':
                continue
            if (nr,nc) in explored or (myload >= self.C and self.grid[nr][nc] == 's'):
                continue
            yield (nr,nc)
     
    # At first find the shortest path 
    def shortestPath(self,begr,begc):
        hp = [(0,begr,begc)]
        #dist = [[None]*self.N for _ in range(self.N)]
        dist = dict()
        #source = [[None]*self.N for _ in range(self.N)]
        source = dict()
        #dist[begr][begc] = 0
        dist[(begr,begc)] = 0

        while hp:
            curdist, r, c = heappop(hp)
            #if curdist > dist[r][c]:
            if curdist > dist[(r,c)]:
                continue
            for nr,nc in self.iterMoves(r,c):
                #eprint(r,c,'exploring ', nr,nc)
                if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                    dist[(nr,nc)] = curdist+1
                    #source[nr][nc] = []
                    source[(nr,nc)] = []
                    heappush(hp,(curdist+1,nr,nc))
                if dist[(nr,nc)] >= (curdist+1):
                    #source[nr][nc].append((r,c))
                    source[(nr,nc)].append((r,c))
        
        #eprint(r,c,'Done',dist)
        return [dist,source]        

    def buildPathToSlime(self,begr,begc,r,c,dist,source,explored):
        curdist = dist[(r,c)]
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
                #self.grid[r][c] = '.' # do not allow others find it
                prev[(begr,begc)] = (rr,cc)
                return [(r,c),prev,'s']
            if rr == begr and cc == begc:
                continue
            for pr,pc in source[(rr,cc)]:
                if (dist[(pr,pc)] + cost + 1) > curdist:
                    continue
                stack.append( (cost+1,pr,pc))
                prev[(pr,pc)] = (rr,cc)
        return None

    def buildPathToDepot(self,depr,depc,r,c,dist,source,explored):
        prev = dict()

        rr,cc = r,c
        while (depr,depc) != (rr,cc):
            if (rr,cc) in source:
                for pr,pc in source[(rr,cc)]:
                    if self.grid[pr][pc] != 's' and (pr,pc) not in explored:
                        prev[(rr,cc)] = (pr,pc)
                        rr,cc = pr,pc
                        break
                else:
                    return None
            else:
                return None
        return [(depr,depc),prev,'d']



    def shortestPathSubGrid(self,begr,begc,limit,explored):
        hp = [(0,begr,begc)]
        dist = dict()
        source = dict()
        dist[(begr,begc)] = 0

        while hp:
            curdist, r, c = heappop(hp)
            if curdist > dist[(r,c)]:
                continue
            if self.grid[r][c] == 's' and (begr,begc) != (r,c):

                p = self.buildPathToSlime(begr,begc,r,c,dist,source,explored)
                if p is not None:
                    return p
                #eprint(begr,begc,'No steps to take!')
                #return None,None
            if curdist > limit:
               return None

            for nr,nc in self.iterMoves(r,c):
                if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                    dist[(nr,nc)] = curdist+1
                    source[(nr,nc)] = []
                    heappush(hp,(curdist+1,nr,nc))
                if dist[(nr,nc)] >= (curdist+1):
                    source[(nr,nc)].append((r,c))
        
        return None


    def calcSubGrid(self,r,c):
        subr,r2 = divmod(r,self.RN)
        subc,c2 = divmod(c,self.RN)
        return (subr,subc),(r2,c2)

    def manhatdist(self,r1,c1,r2,c2):
        return abs(r2-r1)+abs(c2-c1)

    def buildHarvestorSubGrids(self):
        subgrids = dict()
        for h,(r,c) in enumerate(self.har):
            subgrp,unused = self.calcSubGrid(r,c)
            if subgrp not in subgrids:
                subgrids[subgrp] = [h]
            else:
                subgrids[subgrp].append(h)
        return subgrids

    def buildSlimeSubGrids(self, slimes):
        subgrids = dict()
        for i,(r,c) in enumerate(slimes):
            subgrp,unused = self.calcSubGrid(r,c)
            if subgrp not in subgrids:
                subgrids[subgrp] = [i]
            else:
                subgrids[subgrp].append(i)
        return subgrids


    def isNeighborBusy(self, h, moves, limit=3):
        begr,begc = self.har[h]

        for h2 in range(self.H):
            if h!=h2 and moves[h2] is not None:
                r,c = self.har[h2]
                if self.manhatdist(begr,begc,r,c) <= limit:
                    return True
        return False

       

    def shortestPathAB(self,begr,begc,tgtr,tgtc,limit,explored):
        hp = [(manhatdist(self,tgtr,tgtc,begr,begc),0,begr,begc)]
        dist = dict()
        source = dict()
        dist[(begr,begc)] = 0

        while hp:
            ham,curdist, r, c = heappop(hp)
            if curdist > dist[(r,c)]:
                continue
            if self.grid[r][c] == 's' and (begr,begc) != (r,c):

                p = self.buildPathToSlime(begr,begc,r,c,dist,source,explored)
                if p is not None:
                    return p
                #eprint(begr,begc,'No steps to take!')
                #return None,None
            if curdist > limit:
               return None

            for nr,nc in self.iterMoves(r,c):
                if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                    dist[(nr,nc)] = curdist+1
                    source[(nr,nc)] = []
                    heappush(hp,(self.manhatdist(tgtr,tgtc,nr,nc),curdist+1,nr,nc))
                if dist[(nr,nc)] >= (curdist+1):
                    source[(nr,nc)].append((r,c))
        
        return None

    def nextCell(self,r,c,explored,myload,dist):
        if (r,c) not in dist:
            if debug:
                eprint(r,c,'nextCell not found', dist)
        curdist = dist[(r,c)]
        for nr,nc in self.iterMovesGivenExplored(r,c,explored,myload):
            if (nr,nc) not in dist:
                continue
            if dist[(nr,nc)] < curdist:
                return nr,nc
        for nr,nc in self.iterMovesGivenExplored(r,c,explored,myload):
            if (nr,nc) not in dist:
                continue
            if dist[(nr,nc)] <= curdist: # notice smaller equal
                return nr,nc
                
        if debug:
            eprint(r,c,'nextCell check mate')
        return None

    def collectSlime(self,h,explored,myload,unusedDepotBusy):
        r,c = self.har[h]
        if myload >= self.C:
            self.planPath[h] = None
            return None # cannot collect slime

        if self.planPath[h] is None:
            self.planPath[h] = self.shortestPathSubGrid(r,c,self.RN*self.RN,explored)

        if self.planPath[h] is None:
            return None

        (fr,fc),prev,plantype = self.planPath[h]
        if self.grid[fr][fc] != 's': # Slime is gone
            if debug:
                eprint(h,r,c,'path is lost', self.grid[fr][fc])
            self.planPath[h] = None
            return None

        if (r,c) not in prev:
            if debug:
                eprint(h,r,c,'path is broke during collecting slime', plantype)
            self.planPath[h] = None
            return None
        nr,nc = prev[(r,c)]
        if (nr,nc) in explored:
            # wait for other planPath[h] = None
            return None # FIXME should we scatter here ?
        if self.grid[nr][nc] == 's' and myload >= self.C:
            self.planPath[h] = None
            return None # We are full
        assert((r,c) in explored)
        assert(self.grid[nr][nc] != 'd')
        if self.grid[nr][nc] != 'd':
            #explored.remove((r,c))
            explored.add((nr,nc))
        return self.calcDir(nr,nc,r,c)

    def moveToNearestDepot(self,h,explored, myload, depotbusy):
        r,c = self.har[h]

        if self.planPath[h] is not None:
            (fr,fc),prev,actiontp = self.planPath[h]
            if self.grid[fr][fc] != 'd': # dipot is gone
                self.planPath[h] = None

        if self.planPath[h] is None:

            dist = []
            for i in range(self.D):
                if depotbusy[i]:
                    continue
                if self.shortestPathFromDepot[i] is None:
                    continue
                if (r,c) in self.shortestPathFromDepot[i][0]:
                    dist.append( (self.shortestPathFromDepot[i][0][(r,c)], i) )
                else:
                    if debug:
                        eprint(h,r,c,'harvestor does not have shortest path', self.shortestPathFromDepot[i][0])
            if debug:
                eprint(h,r,c,'move to neareest', dist, depotbusy)
            if not dist:
                return None
            unused,nearest = min(dist)
            if debug:
                eprint(h,r,c,'found nearest', nearest)
            fr,fc = self.depots[nearest]
            disttable,sourcetable = self.shortestPathFromDepot[nearest]
            
            self.planPath[h] = self.buildPathToDepot(fr,fc,r,c,disttable,sourcetable,explored)

        if debug:
            eprint(h,r,c,'plan', self.planPath[h])
        if self.planPath[h] is None:
            return None

        (fr,fc),prev,plantp = self.planPath[h]
        
        if debug:
            eprint(h,r,c,'plan fc,fr', fr,fc)
        if self.grid[fr][fc] != 'd': # dipot is gone
            if debug:
                eprint(h,r,c,'path is lost', self.grid[fr][fc])
            self.planPath[h] = None
            return None

        if (r,c) not in prev:
            if debug:
                eprint(h,r,c,'path is broke while moving to nearest depot', plantp)
            self.planPath[h] = None
            return None
        nr,nc = prev[(r,c)]
        if (nr,nc) in explored:
            # wait for other planPath[h] = None
            if debug:
                eprint(h,r,c,'move is occupied', nr,nc)
            return None # FIXME should we scatter here ?
        if self.grid[nr][nc] == 's' and myload >= self.C:
            self.planPath[h] = None
            if debug:
                eprint(h,r,c,'Cannot collect slime', nr.nc)
            return None # We are full
        assert((r,c) in explored)
        if self.grid[nr][nc] != 'd':
            #explored.remove((r,c))
            explored.add((nr,nc))
        if debug:
            eprint(h,r,c,'path found next move', self.calcDir(nr,nc,r,c))
        return self.calcDir(nr,nc,r,c)

    def moveAwayFromNearestDepot(self,h,explored, capacity, depotbusy):
        r,c = self.har[h]
        dist = []
        for i in range(self.D):
            if depotbusy[i]:
                continue
            if (r,c) in self.shortestPathFromDepot[i][0]:
                dist.append( (self.shortestPathFromDepot[i][0][(r,c)], i) )
        if not dist:
            return None
        unused,nearest = min(dist)

        dist = self.shortestPathFromDepot[nearest][0]
        if (r,c) not in dist: # we entered into a depot
            for nr,nc in self.iterMovesGivenExplored(r,c, explored, capacity):
                explored.add((nr,nc))
                return self.calcDir(nr,nc,r,c)
            return None
            
        for nr,nc in self.iterMovesGivenExplored(r,c, explored, capacity):
            if (nr,nc) not in dist: # do not enter into a depot
                continue
            if dist[(nr,nc)] > dist[(r,c)]:
                assert((r,c) in explored)
                if self.grid[nr][nc] != 'd':
                    #explored.remove((r,c))
                    explored.add((nr,nc))
                return self.calcDir(nr,nc,r,c)

        for nr,nc in self.iterMovesGivenExplored(r,c, explored, capacity):
            if (nr,nc) not in dist: # do not enter into a depot
                continue
            if dist[(nr,nc)] >= dist[(r,c)]: # notice >= here
                assert((r,c) in explored)
                if self.grid[nr][nc] != 'd':
                    #explored.remove((r,c))
                    explored.add((nr,nc))
                return self.calcDir(nr,nc,r,c)


        return None


    def moveToNearestGarrage(self,h,explored, myload, depotbusy):
        r,c = self.har[h]
        nearest,nearestg = None,None
        for i,g in enumerate(self.garrages):
            if g is not None:
                if nearest is None or self.manhatdist(nearestg[0],nearestg[1],r,c) >  self.manhatdist(g[0],g[1],r,c):
                    nearest = i
                    nearestg = g
        if nearest is None or self.shortestPathFromGarrages[nearest] is None:
            return None

        # now find the path to nearest depot
        source = self.shortestPathFromGarrages[nearest][1]
        #eprint(source,r,c,source[r][c])
        if (r,c) not in source: # path broke
            return None
        
        lr,lc = source[(r,c)][0]
        for lr,lc in source[(r,c)]:
            if (lr,lc) in explored or (myload >= self.C and self.grid[lr][lc] == 's'):
                continue
            assert((r,c) in explored)
            if self.grid[lr][lc] != 'd':
                #explored.remove((r,c))
                explored.add((lr,lc))
            return self.calcDir(lr,lc,r,c)
        return None

    def sendMoves(self, moveCmds):
        if debug:
            eprint('============================================')
        harvpos = set()
        cmd = []
        dname = ['R','D','L','U']
        # Move each harvester
        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                d = moveCmds[h]
                cmd.append(self.harstr[h])
                cmd.append(dname[d])

                if debug:
                    # debug begins
                    curgrid = self.grid[r][:]
                    eprint(curgrid,r,c)
                    curgrid[c] = '!'
                    eprint(curgrid,r,c)
                    # debug ends

                nr = r + self.dr[d]
                nc = c + self.dc[d]
                if self.grid[nr][nc] == 'd':
                    self.planPath[h] = None
                else:
                    self.har[h] = [nr,nc]
                
                rr,cc = self.har[h]
                #explored.add((nr,nc))
                if debug:
                    # debug begins
                    curgrid = self.grid[rr][:]
                    eprint(curgrid,'A',rr,cc)
                    curgrid[cc] = '!'
                    eprint(curgrid,'A',rr,cc)
                    # debug ends

                if debug:
                    assert((rr,cc) not in harvpos)
                    harvpos.add((rr,cc))
                    assert(not( nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W'))
            else:
                cmd.append(self.harstr[h])
                cmd.append('X')
                rr,cc = self.har[h]
                if debug:
                    #assert((rr,cc) not in harvpos)
                    harvpos.add((rr,cc))

        self.tester.pushCmd(cmd)

        self.load = self.tester.parseLoad()

        # Read the updated grid
        self.tester.parseGrid(self.grid)

        # fix bad depots and harvestor position
        changed = False
        for i,(dr,dc) in enumerate(self.depots):
            if self.grid[dr][dc] != 'd':
                if not self.depotbad[i]:
                    self.depotbad[i] = True
                    changed = True

        if changed:
            self.buildShortestPathFromDepot()

 
    def run(self,turn):

        explored = set()

        # find the slimes and nearest harvestors
        slimes = []
        slimeId = dict()
        for r in range(self.N):
          for c in range(self.N):
            if self.grid[r][c] == 's':
                slimeId[(r,c)] = len(slimes)
                slimes.append((r,c))
                # return to nearest depot ?
            elif self.grid[r][c] == 'W':# or grid[r][c] == 'd':
                explored.add((r,c))
                

        depotbusy = self.depotbad[:]

        for h,(r,c) in enumerate(self.har):
            explored.add((r,c))

        moveCmds = [None]*self.H

        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if self.planPath[h] is not None:
                if self.planPath[h][2] == 'd':
                    moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                    if debug:
                        eprint('Harvester ',h,r,c, 'moving to nearestet depot', moveCmds[h])
                elif self.planPath[h][2] == 's':
                    moveCmds[h] = self.collectSlime(h,explored,self.load[h],depotbusy)
                    if debug:
                        eprint('Harvester ',h,r,c, 'Collecting slime', moveCmds[h])
                 

        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if self.load[h]>=self.C:
                moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                if debug:
                    eprint('Harvester ',h,r,c, 'moving to nearestet depot via new path', moveCmds[h])

            elif slimes:
                moveCmds[h] = self.collectSlime(h,explored,self.load[h],None)
                if debug:
                    eprint('Harvester ',h,r,c, 'Collecting slime in new path', moveCmds[h])
                 
        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.load[h]:
                if self.isNeighborBusy(h, moveCmds):
                    continue
                moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                if debug:
                    eprint('Harvester ',h,r,c, 'Moving to nearest depot', moveCmds[h])
            else:
                moveCmds[h] = self.moveAwayFromNearestDepot(h,explored,self.load[h],depotbusy)
                if debug:
                    eprint('Harvester ',h,r,c, 'Moving away', moveCmds[h])
 

        #slimeSubGrids = self.buildSlimeSubGrids(slimes)
     
        self.sendMoves(moveCmds)

class AutoTester:

    def __init__(self,N,C,H):
        self.N = N
        self.C = C
        self.H = H

    def setupHarvester(self):
        har = [(0,0)]*self.H
        return har
        
    def parseGrid(self,grid):
        pass

    def parseLoad(self):
        return [0]*H

    def pushCmd(self,cmd):
        pass

class StdTester:
    def __init__(self):
        # Read in N (grid size), C (max load capacity), and H (number of harvesters)
        self.N = int(input())
        self.C = int(input())
        self.H = int(input())
        if debug:
            eprint('N,C,H',self.N,self.C,self.H);

    def setupHarvester(self):
        har = [(0,0)]*self.H
        for h in range(self.H):
          row, col = input().split(" ")
          har[h] = [int(row),int(col)]

        return har
 
    def parseGrid(self,grid):
        # Read the starting grid configuration
        for r in range(self.N):
          for c in range(self.N):
            grid[r][c] = input()

    def parseLoad(self):
        # Read the elapsed time
        tm = int(input())
        load = [0]*self.H
        # Read the number of fuel carried by each harvester
        for h in range(self.H):
            load[h] = int(input())
        return load

    def pushCmd(self,cmd):
        assert(len(cmd) == self.H*2)
        cmdstr = ' '.join(cmd)+" "
        if debug:
            #sys.stderr.write(cmdstr)
            eprint(cmdstr)
        #time.sleep(1/10)
        # Output the command for the turn
        #print(cmdstr,flush=False)
        #print(cmdstr)
        #print(cmdstr,flush=True,end='')
        #print(cmdstr,end='')
        #sys.stdout.write(cmdstr)
        print(cmdstr)
        sys.stdout.flush()
        #print()
        #sys.stdout.flush()


if __name__ == "__main__":

    #tester = AutoTester() # or StdTester
    tester = StdTester()
    bsalg = BioSlime(tester)
    bsalg.setup()

    # Simulate 1000 turns
    for turn in range(1000):
        bsalg.run(turn)



