
import copy
import random
import argparse
import time
import sys
from collections import defaultdict
from heapq import heappop,heappush,heapify


bestParams = [None, None, None, None, None, None, None, None, None, None, [None, [None, None, None, None, None, None, None, None, ('6', '8'), ('6', '1'), ('4', '1'), ('4', '1'), ('5', '1'), ('6', '8'), ('6', '1'), ('6', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '8'), ('7', '1'), ('7', '1'), ('7', '1'), ('7', '1'), ('5', '1'), ('5', '9'), ('4', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('6', '1'), ('5', '1'), ('6', '1'), ('5', '1'), ('7', '9'), ('6', '1'), ('6', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('6', '1'), ('7', '1'), ('5', '1'), ('5', '1'), ('4', '8'), ('4', '1'), ('7', '1'), ('7', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('5', '8'), ('4', '9'), ('4', '1'), ('6', '1'), ('7', '1'), ('6', '8'), ('6', '1'), ('7', '9'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '8'), ('7', '8'), ('5', '8'), ('7', '8'), ('7', '1'), ('5', '8'), ('6', '9'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '8'), ('5', '8'), ('4', '9'), ('5', '9'), ('7', '1'), ('5', '1'), ('7', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('7', '1'), ('4', '1'), ('4', '1'), ('4', '1'), ('6', '1'), ('5', '9'), ('7', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('7', '8'), ('7', '1'), ('5', '1'), ('4', '9'), ('6', '8'), ('6', '1'), ('4', '1'), ('5', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('4', '8'), ('7', '1'), ('4', '1'), ('4', '1'), ('6', '1'), ('4', '1'), ('4', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '8'), ('5', '1'), ('6', '1'), ('4', '1'), ('5', '1'), ('5', '1'), ('7', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('5', '1'), ('4', '1'), ('6', '1'), ('5', '1'), ('6', '9'), ('4', '8'), ('7', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('5', '8'), ('5', '8'), ('7', '8'), ('6', '8'), ('7', '8'), ('4', '8'), ('5', '8'), ('5', '9'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('5', '8'), ('6', '1'), ('7', '9'), ('7', '1'), ('6', '1'), ('5', '9'), ('4', '9'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '9'), ('7', '9'), ('4', '8'), ('7', '8'), ('6', '9'), ('4', '1'), ('7', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('4', '1'), ('7', '9'), ('4', '8'), ('7', '8'), ('5', '8'), ('7', '1'), ('7', '8'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('7', '1'), ('6', '9'), ('5', '8'), ('6', '1'), ('4', '8'), ('4', '1'), ('7', '9'), ('6', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '9'), ('7', '8'), ('7', '9'), ('7', '9'), ('5', '8'), ('5', '9'), ('6', '8'), ('5', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('5', '1'), ('4', '1'), ('7', '1'), ('6', '1'), ('7', '1'), ('7', '8'), ('7', '8'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('4', '8'), ('7', '1'), ('6', '1'), ('6', '1'), ('6', '9'), ('4', '1'), ('6', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('4', '1'), ('7', '1'), ('5', '1'), ('5', '9'), ('5', '1'), ('7', '1'), ('5', '1'), ('6', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '8'), ('7', '8'), ('6', '1'), ('7', '1'), ('5', '8'), ('5', '1'), ('4', '8'), ('4', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '9'), ('7', '8'), ('4', '9'), ('4', '1'), ('5', '9'), ('5', '9'), ('6', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('7', '9'), ('6', '9'), ('7', '8'), ('7', '1'), ('6', '1'), ('4', '9'), ('7', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('6', '1'), ('6', '1'), ('7', '9'), ('5', '1'), ('5', '1'), ('4', '1'), ('4', '9'), ('6', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '1'), ('4', '8'), ('5', '8'), ('5', '1'), ('4', '1'), ('6', '9'), ('5', '8'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('7', '8'), ('5', '8'), ('7', '8'), ('6', '9'), ('4', '8'), ('7', '9'), ('7', '8'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('6', '1'), ('5', '9'), ('5', '1'), ('5', '9'), ('5', '8'), ('7', '8'), ('6', '1'), ('7', '8'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('5', '1'), ('5', '1'), ('4', '1'), ('4', '1'), ('4', '8'), ('4', '1'), ('6', '1'), ('5', '8'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('4', '1'), ('6', '1'), ('7', '1'), ('6', '8'), ('6', '1'), ('5', '1'), ('6', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('6', '1'), ('7', '1'), ('6', '1'), ('5', '1'), ('4', '1'), ('7', '8'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '1'), ('6', '8'), ('7', '1'), ('5', '1'), ('7', '1'), ('7', '1'), ('6', '1'), ('7', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('7', '1'), ('5', '1'), ('5', '1'), ('6', '1'), ('4', '1'), ('5', '1'), ('5', '1'), ('6', '8'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('5', '1'), ('7', '9'), ('7', '1'), ('4', '1'), ('7', '1'), ('4', '1'), ('5', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '8'), ('6', '1'), ('4', '9'), ('5', '1'), ('5', '8'), ('7', '1'), ('5', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('4', '1'), ('4', '1'), ('5', '1'), ('4', '1'), ('6', '1'), ('4', '1'), ('4', '1'), ('4', '1'), None, None, None, None, None], None, None, None, None, None, None], [None, [None, None, None, None, None, None, None, None, ('5', '1'), ('4', '1'), ('4', '1'), ('6', '9'), ('4', '1'), ('4', '1'), ('7', '1'), ('5', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('5', '1'), ('5', '1'), ('7', '1'), ('6', '1'), ('7', '1'), ('5', '1'), ('4', '8'), ('7', '8'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '1'), ('5', '1'), ('6', '1'), ('6', '1'), ('5', '1'), ('5', '8'), ('7', '1'), ('7', '1'), None, None, None, None, None], [None, None, None, None, None, None, None, None, ('7', '9'), ('7', '1'), ('7', '8'), ('4', '1'), ('7', '9'), ('4', '1'), ('4', '1'), ('7', '8'), None, None, None, None, None], None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None], [None, None, None, None, None, None, None, None, None, None, None]]




debug = False
debugStrategy=False
debugMove = False
debugCalStrategy=True
debugGrid = True
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

SLIME,WALL,EMPTY,DEPOT,HARVESTER = 's','W','.','d','H'
MAXIMUM_ALLOWED_CAPACITY=14
MIN_HARVESTOR_PER_DEPOT=4

class CalibrationStrategyRatio:

    def __init__(self, N, C, H, PARAM_DIV, PARAM_CLEANUP_TURN):
        self.N = N
        self.C = C
        self.H = H
        self.PARAM_DIV = PARAM_DIV
        self.PARAM_CLEANUP_TURN = PARAM_CLEANUP_TURN


        # calibration logic
        self.prevScore = 0
        self.prevNumSlimes = 0
        self.applcableCapacity = min(2,self.C)

    def setupDepot(self,depotbad,depotscore):
        self.depotbad = depotbad
        self.depotscore = depotscore
        self.D = len(self.depotbad)

    def setupHarvester(self, harvesterStuck):
        self.harvesterStuck = harvesterStuck

    def autoParam(self):

        '''
        if self.N < len(bestParams) and bestParams[self.N] is not None:
            if self.D < len(bestParams[self.N]) and bestParams[self.N][self.D] is not None:
                if self.H < len(bestParams[self.N][self.D]) and bestParams[self.N][self.D][self.H] is not None:
                    self.PARAM_DIV = bestParams[self.N][self.D][self.H] 
                    if debugCalStrategy:
                        eprint('Found auto param', self.PARAM_DIV)

        '''
        if debugCalStrategy:
            eprint('Auto param', self.PARAM_DIV)


    def calculateScore(self, numSlimes):
        
        totalScore = self.N*self.N
        totalScore -= numSlimes
        for d in range(self.D):
            totalScore += self.depotscore[d]
        return totalScore

    def calculateApplicableCapacity(self, turn, curNumSlimes):

        if 0 == turn:
            self.prevScore = self.calculateScore(curNumSlimes)
            self.prevNumSlimes = curNumSlimes
            return self.applcableCapacity

        curScore = self.calculateScore(curNumSlimes)

        numharvesterStuck = 0
        for x in self.harvesterStuck:
            if x:
                numharvesterStuck += 1


        if turn >= self.PARAM_CLEANUP_TURN: # At the end use highest capacity
            self.applcableCapacity = min(MAXIMUM_ALLOWED_CAPACITY, self.C)
            if debugCalStrategy and (turn % 40) == 0:
                eprint(turn, 'CLEANUP Applicable capacity', self.applcableCapacity,'numSlimes',curNumSlimes,'curScore',curScore,'numharvesterStuck',numharvesterStuck)
            return self.applcableCapacity

        if (turn % 40) != 0:
            return self.applcableCapacity

        numharvesterStuck = 0
        for x in self.harvesterStuck:
            if x:
                numharvesterStuck += 1

        #activeharvesters = self.H-numharvesterStuck
        activeharvesters = self.H

        if activeharvesters:
            ratio = curNumSlimes/activeharvesters
            self.applcableCapacity = min(MAXIMUM_ALLOWED_CAPACITY,  min(max(0,int(ratio-1)),self.C) )
        else:
            self.applcableCapacity = min(MAXIMUM_ALLOWED_CAPACITY, self.C)


        self.prevScore = curScore
        self.prevNumSlimes = curNumSlimes

        if debugCalStrategy:
            eprint(turn, 'Applicable capacity', self.applcableCapacity,'numSlimes',curNumSlimes,'curScore',curScore,'numharvesterStuck',numharvesterStuck)
        return self.applcableCapacity
 
class CalibrationStrategy:

    def __init__(self, N, C, H, PARAM_DIV, PARAM_CLEANUP_TURN):
        self.N = N
        self.C = C
        self.H = H
        self.PARAM_DIV = PARAM_DIV
        self.PARAM_CLEANUP_TURN = PARAM_CLEANUP_TURN


        # calibration logic
        self.prevScore = 0
        self.prevNumSlimes = 0
        self.applcableCapacity = min(2,self.C)

    def setupDepot(self,depotbad,depotscore):
        self.depotbad = depotbad
        self.depotscore = depotscore
        self.D = len(self.depotbad)

    def setupHarvester(self, harvesterStuck):
        self.harvesterStuck = harvesterStuck

    def autoParam(self):

        '''
        if self.N < len(bestParams) and bestParams[self.N] is not None:
            if self.D < len(bestParams[self.N]) and bestParams[self.N][self.D] is not None:
                if self.H < len(bestParams[self.N][self.D]) and bestParams[self.N][self.D][self.H] is not None:
                    self.PARAM_DIV = bestParams[self.N][self.D][self.H] 
                    if debugCalStrategy:
                        eprint('Found auto param', self.PARAM_DIV)
        '''

        if debugCalStrategy:
            eprint('Auto param', self.PARAM_DIV)


    def calculateScore(self, numSlimes):
        
        totalScore = self.N*self.N
        totalScore -= numSlimes
        for d in range(self.D):
            totalScore += self.depotscore[d]
        return totalScore

    def calculateApplicableCapacity(self, turn, curNumSlimes):

        if 0 == turn:
            self.prevScore = self.calculateScore(curNumSlimes)
            self.prevNumSlimes = curNumSlimes
            return self.applcableCapacity

        if turn >= self.PARAM_CLEANUP_TURN: # At the end use highest capacity
            self.applcableCapacity = self.C
            return self.applcableCapacity

        if (turn % 40) != 0:
            return self.applcableCapacity

        curScore = self.calculateScore(curNumSlimes)

        if curNumSlimes < self.prevNumSlimes:
            if (self.prevNumSlimes-curNumSlimes) >= (curNumSlimes/self.PARAM_DIV):
                self.applcableCapacity = self.applcableCapacity>>1
                #if self.applcableCapacity < 2:
                #    self.applcableCapacity = 2
        else:
            if (curNumSlimes-self.prevNumSlimes) >= (self.prevNumSlimes/self.PARAM_DIV):
                self.applcableCapacity = min(self.C,(self.applcableCapacity<<1))


        self.prevScore = curScore
        self.prevNumSlimes = curNumSlimes

        if debugCalStrategy:
            eprint(turn, 'Applicable capacity', self.applcableCapacity,'numSlimes',curNumSlimes,'curScore',curScore)
        return self.applcableCapacity
 

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
        self.turn = 0
        self.wanderMoves = [None]*self.H
        self.slimes = []
        self.slimeId = dict()
        self.depotAffinity = [None]*self.H
        self.dumpingToDepot = [False]*self.H
        self.calStrategy = CalibrationStrategyRatio(self.N,self.C,self.H,3,800)
        self.harvesterStuck = [False]*self.H

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

        if self.N < len(bestParams) and bestParams[self.N] is not None:
            if self.D < len(bestParams[self.N]) and bestParams[self.N][self.D] is not None:
                if self.H < len(bestParams[self.N][self.D]) and bestParams[self.N][self.D][self.H] is not None:
                    MIN_HARVESTOR_PER_DEPOT,MAXIMUM_ALLOWED_CAPACITY = bestParams[self.N][self.D][self.H] 
                    if debugCalStrategy:
                        eprint('Found auto param',  MIN_HARVESTOR_PER_DEPOT,MAXIMUM_ALLOWED_CAPACITY)


        self.depotbad = [False]*self.D
        self.depotscore = [0]*self.D
        self.calStrategy.setupDepot(self.depotbad,self.depotscore)
        self.calStrategy.setupHarvester(self.harvesterStuck)

        self.calStrategy.autoParam()

        # This path will be useful to return to depot
        self.buildShortestPathFromDepot()

        eprint('-N',self.N,'-H',self.H,'-C',self.C,'-D',self.D)

    def buildShortestPathFromDepot(self):
        self.shortestPathFromDepot = [None]*self.D

        numDepots = 0
        for i,(r,c) in enumerate(self.depots):
            if not self.depotbad[i]:
                self.shortestPathFromDepot[i] = self.shortestPath(r,c)
                numDepots += 1

        self.depotAffinity = [None]*self.H
        if numDepots <= 0:
            return
        harPerDepot = (self.H//numDepots)+1
        if harPerDepot < MIN_HARVESTOR_PER_DEPOT:
            harPerDepot = MIN_HARVESTOR_PER_DEPOT # try to keep harvesters concentrated
        for i,(r,c) in enumerate(self.depots):
            if not self.depotbad[i]:
                dist = self.shortestPathFromDepot[i][0]
                hp = []
                for h in range(self.H):
                    if self.depotAffinity[h] is not None:
                        continue
                    hr,hc = self.har[h]
                    if (hr,hc) in dist:
                        hp.append((dist[(hr,hc)],h))
                heapify(hp)
                if len(hp) < (harPerDepot+ (harPerDepot>>1)):
                    harPerDepot = len(hp)
                numHar = 0
                while hp and numHar < harPerDepot:
                    unused, h = heappop(hp)
                    self.depotAffinity[h] = i
                    numHar += 1
        

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

    def iterMovesFindDepots(self,r,c,explored,myload):
        for d in range(4):
            nr = r + self.dr[d]
            nc = c + self.dc[d]
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W':
                continue
            if (nr,nc) in explored or (myload >= self.C and self.grid[nr][nc] == 's'):
                continue
            yield (nr,nc)

    def iterMovesAllowTgt(self,r,c,tgtr,tgtc,explored,myload):
        for d in range(4):
            nr = r + self.dr[d]
            nc = c + self.dc[d]
            if (nr,nc) == (tgtr,tgtc):
                yield (nr,nc)
                continue
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W' or self.grid[nr][nc] == 'd':
                continue
            if (nr,nc) in explored or (myload >= self.C and self.grid[nr][nc] == 's'):
                continue
            yield (nr,nc)
 

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

    def buildPathToGoal(self,begr,begc,r,c,dist,source,explored,goal):
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
                return [(r,c),prev,goal]
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

    def shortestPathToDepotAny(self,h,limit,explored,myload):
        begr,begc = self.har[h]
        hp = [(0,begr,begc)]
        dist = dict()
        source = dict()
        dist[(begr,begc)] = 0

        #if debug:
        #    eprint(begr,begc,'shortestPathToDepot~~~~ ')
        while hp:
            curdist, r, c = heappop(hp)
            if curdist > dist[(r,c)]:
                continue
            if self.grid[r][c] == 'd' and (begr,begc) != (r,c):
                #if debug:
                #    eprint(begr,begc,'shortestPathToDepot found depot', r,c)

                p = self.buildPathToGoal(begr,begc,r,c,dist,source,explored,'d')
                if p is not None:
                    return p
                #if debug:
                #    eprint(begr,begc,'shortestPathToDepot No path to depot', r,c)
                #eprint(begr,begc,'No steps to take!')
                #return None,None
            #if curdist > limit:
            #   return None

            for nr,nc in self.iterMovesFindDepots(r,c,explored,myload):
                if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                    dist[(nr,nc)] = curdist+1
                    source[(nr,nc)] = []
                    heappush(hp,(curdist+1,nr,nc))
                if dist[(nr,nc)] >= (curdist+1):
                    source[(nr,nc)].append((r,c))
        
        return None

    def shortestPathToDepot(self,h,limit,explored,myload,depotbusy):
        begr,begc = self.har[h]
        
        depotidx = self.depotAffinity[h]
        if depotidx is None:
            hp = []
            for i,(dr,dc) in enumerate(self.depots):
                if self.depotbad[i]:
                    continue
                hp.append((self.manhatdist(dr,dc,begr,begc),i))
            
            if hp:
                unused,depotidx = min(hp)

        if depotidx is not None:
            dr,dc = self.depots[depotidx]
            ret = self.shortestPathAB(begr,begc,dr,dc,limit,explored,myload)
            ''' Switching affinity is not good
            if ret is None:
                for otherdepotidx,(dr,dc) in enumerate(self.depots):
                    if self.depotbad[otherdepotidx]:
                        continue
                    ret = self.shortestPathAB(begr,begc,dr,dc,limit,explored,myload)
                    if ret is not None:
                        self.depotAffinity[h] = otherdepotidx
                        break
            '''
            if ret is None:
                self.harvesterStuck[h] = True
            else:
                self.harvesterStuck[h] = False
            return ret
        return None



    def shortestPathToSlime(self,h,limit,explored,myload):
        begr,begc = self.har[h]
        # we need to return to depot after grabbing slime
        depotidx = self.depotAffinity[h]
        if depotidx is None:
            depotidx = 0
        dr,dc = self.depots[depotidx]

        tr,tc = dr,dc

        for h2,(r2,c2) in enumerate(self.har):
            if h2 != h:
                if (self.manhatdist(begr,begc,r2,c2)+self.manhatdist(tr,tc,r2,c2)) < (self.manhatdist(begr,begc,dr,dc)+self.manhatdist(tr,tc,dr,dc)):
                    dr,dc = r2,c2
        

        hp = []
        '''
        for i,(sr,sc) in enumerate(self.slimes):
            hp.append((self.manhatdist(sr,sc,begr,begc)+self.manhatdist(sr,sc,dr,dc),i))
        '''

        MAXGRID,unused = self.calcSubGrid(self.N,self.N)[0]
        grids = [(0,self.calcSubGrid(begr,begc)[0])]
        exp = set()
        prevdist = 0
        while grids:
            curdist,(subgr,subgc) = heappop(grids)
            exp.add( (subgr,subgc) )
            if curdist > prevdist and hp:
                break # early exit
            prevdist = curdist
            if (subgr,subgc) in self.slimeSubGrids:
                for idx in self.slimeSubGrids[(subgr,subgc)]:
                    sr,sc = self.slimes[idx]
                    hp.append((self.manhatdist(sr,sc,begr,begc)+self.manhatdist(sr,sc,dr,dc),idx))
            
            for subgr2,subgc2 in [(subgr,subgc-1),(subgr-1,subgc-1),(subgr-1,subgc),(subgr-1,subgc+1),(subgr,subgc+1),(subgr+1,subgc+1),(subgr+1,subgc),(subgr+1,subgc-1)]:
                if (subgr2,subgc2) in exp:
                    continue
                if subgr2 < 0 or subgc2 < 0 or subgr2 > MAXGRID or subgc2 > MAXGRID:
                    continue
                exp.add( (subgr2,subgc2) )
                heappush(grids, (curdist+1,(subgr2,subgc2)) )
            
        
        if hp:
            unused,idx = min(hp)
            sr,sc = self.slimes[idx]
            return self.shortestPathAB(begr,begc,sr,sc,limit,explored,myload)
        return None

    def shortestPathToSlimeAny(self,h,limit,explored):
        begr,begh = self.har[h]
        
        hp = [(0,begr,begc)]
        dist = dict()
        source = dict()
        dist[(begr,begc)] = 0

        while hp:
            curdist, r, c = heappop(hp)
            if curdist > dist[(r,c)]:
                continue
            if self.grid[r][c] == 's' and (begr,begc) != (r,c):

                p = self.buildPathToGoal(begr,begc,r,c,dist,source,explored,'s')
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

    def buildHarvesterSubGrids(self):
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

       

    def shortestPathAB(self,begr,begc,tgtr,tgtc,limit,explored,myload):
        hp = [(self.manhatdist(tgtr,tgtc,begr,begc),0,begr,begc)]
        dist = dict()
        source = dict()
        dist[(begr,begc)] = 0

        while hp:
            ham,curdist, r, c = heappop(hp)
            if curdist > dist[(r,c)]:
                continue
            if (r,c) == (tgtr,tgtc) and (begr,begc) != (r,c):

                p = self.buildPathToGoal(begr,begc,r,c,dist,source,explored,self.grid[r][c])
                if p is not None:
                    return p
                #eprint(begr,begc,'No steps to take!')
                #return None,None
            if curdist > limit:
               return None

            for nr,nc in self.iterMovesAllowTgt(r,c,tgtr,tgtc,explored,myload):
                if (nr,nc) not in dist or dist[(nr,nc)] > (curdist+1):
                    dist[(nr,nc)] = curdist+1
                    source[(nr,nc)] = []
                    heappush(hp,(self.manhatdist(tgtr,tgtc,nr,nc),curdist+1,nr,nc))
                if dist[(nr,nc)] >= (curdist+1):
                    source[(nr,nc)].append((r,c))
        
        return None

    def collectSlime(self,h,explored,myload,unusedDepotBusy):
        r,c = self.har[h]
        if myload >= self.C:
            self.planPath[h] = None
            return None # cannot collect slime

        if self.planPath[h] is None:
            self.planPath[h] = self.shortestPathToSlime(h,self.RN*self.RN,explored,myload)
        elif (self.turn%4) == 0: # re-evaluate
            self.planPath[h] = self.shortestPathToSlime(h,self.RN*self.RN,explored,myload)

        if self.planPath[h] is None:
            return None

        (fr,fc),prev,plantype = self.planPath[h]
        if self.grid[fr][fc] != 's': # Slime is gone
            if debugStrategy:
                eprint(h,r,c,'path is lost', self.grid[fr][fc])
            self.planPath[h] = None
            return None

        if (r,c) not in prev:
            if debugStrategy:
                eprint(h,r,c,'path is broke during collecting slime', plantype)
            self.planPath[h] = None
            return None
        nr,nc = prev[(r,c)]
        if (nr,nc) in explored:
            # wait for other planPath[h] = None
            if self.turn%4 == 0:
                self.planPath[h] = None # find new path
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

        for nr,nc in self.iterMovesFindDepots(r,c,explored,myload):
            if self.grid[nr][nc] == 'd':
                self.planPath[h] = None
                explored.add((nr,nc))
                return self.calcDir(nr,nc,r,c)

        if self.planPath[h] is not None:
            (fr,fc),prev,actiontp = self.planPath[h]
            if self.grid[fr][fc] != 'd': # dipot is gone
                self.planPath[h] = None

        if self.planPath[h] is None:
            self.planPath[h] = self.shortestPathToDepot(h,self.N*self.N,explored,myload,depotbusy)

        elif (self.turn%4) == 0: # re-evaluate
            self.planPath[h] = self.shortestPathToDepot(h,self.N*self.N,explored,myload,depotbusy)

        if debugStrategy:
            eprint(h,r,c,'move to depot plan') #, self.planPath[h])
        if self.planPath[h] is None:
            return None

        (fr,fc),prev,plantp = self.planPath[h]
        
        if debugStrategy:
            eprint(h,r,c,'plan fc,fr', fr,fc)
        if self.grid[fr][fc] != 'd': # dipot is gone
            if debugStrategy:
                eprint(h,r,c,'path is lost', self.grid[fr][fc])
            self.planPath[h] = None
            return None

        if (r,c) not in prev:
            if debugStrategy:
                eprint(h,r,c,'path is broke while moving to nearest depot', plantp)
            self.planPath[h] = None
            return None
        nr,nc = prev[(r,c)]
        if (nr,nc) in explored:
            # wait for other planPath[h] = None
            if debugStrategy:
                eprint(h,r,c,'move is occupied', nr,nc)
            if self.turn%4 == 0:
                self.planPath[h] = None # find new path
            return None # FIXME should we scatter here ?
        if self.grid[nr][nc] == 's' and myload >= self.C:
            self.planPath[h] = None
            if debugStrategy:
                eprint(h,r,c,'Cannot collect slime', nr,nc)
            return None # We are full
        assert((r,c) in explored)
        if self.grid[nr][nc] != 'd':
            #explored.remove((r,c))
            explored.add((nr,nc))
        if debugStrategy:
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

    def moveAwayFromSlimeWhenSurrounded(self,h,explored, capacity, depotbusy):
        r,c = self.har[h]

        freeMoves = []
        for d in range(4):
            nr = r + self.dr[d]
            nc = c + self.dc[d]
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W' or self.grid[nr][nc] == 'S':
                continue
            freeMoves.append((nr,nc))

        if 1 == len(freeMoves):
            ret = self.moveToNearestDepot(self,h,explored,capacity,depotbusy)
            if ret is None:
                explored.add(freeMoves[-1])
                return freeMoves[-1]
        return None

    def wander(self, h, explored, myload, depotbusy):
        r,c = self.har[h]

        if self.wanderMoves[h] is None:
            self.wanderMoves[h] = 0
        
        for d in range(4):
            nd = (self.wanderMoves[h]+d)%4
            nr = r+self.dr[nd]
            nc = c+self.dr[nd]
            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]=='W' or self.grid[nr][nc] == 'd':
                continue
            if (nr,nc) in explored or (myload >= self.C and self.grid[nr][nc] == 's'):
                continue
            
            self.wanderMoves[h] = nd
            explored.add((nr,nc))
            return self.calcDir(nr,nc,r,c)
        return None
        

    def sendMoves(self, moveCmds):
        if debug or debugMove or debugStrategy:
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

                if debugMove:
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
                if debugMove:
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

        # fix bad depots and harvester position
        changed = False
        for i,(dr,dc) in enumerate(self.depots):
            if self.grid[dr][dc] != 'd':
                if not self.depotbad[i]:
                    self.depotbad[i] = True
                    changed = True

        if changed:
            self.buildShortestPathFromDepot()

 
    def run(self,turn):

        self.turn = turn
        explored = set()

        # find the slimes and nearest harvesters
        self.slimes = []
        self.slimeId = dict()
        for r in range(self.N):
          for c in range(self.N):
            if self.grid[r][c] == 's':
                self.slimeId[(r,c)] = len(self.slimes)
                self.slimes.append((r,c))
                # return to nearest depot ?
            elif self.grid[r][c] == 'W':# or grid[r][c] == 'd':
                explored.add((r,c))
                
        self.slimeSubGrids = self.buildSlimeSubGrids(self.slimes)

        applcableCapacity = self.calStrategy.calculateApplicableCapacity(turn, len(self.slimes))
        depotbusy = self.depotbad[:]

        for h,(r,c) in enumerate(self.har):
            explored.add((r,c))

        moveCmds = [None]*self.H

        totalLoad = sum(self.load)
        if not self.slimes and 0 == totalLoad:
            self.sendMoves(moveCmds)
            return
            
        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            moveCmds[h] = self.moveAwayFromSlimeWhenSurrounded(h,explored,self.load[h],depotbusy) 

        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if self.planPath[h] is not None:
                if self.planPath[h][2] == 'd':
                    moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                    if debugStrategy:
                        eprint('Harvester ',h,r,c, 'moving to nearestet depot', moveCmds[h])
                elif self.planPath[h][2] == 's':
                    moveCmds[h] = self.collectSlime(h,explored,self.load[h],depotbusy)
                    if debugStrategy:
                        eprint('Harvester ',h,r,c, 'Collecting slime', moveCmds[h])
                 

        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if self.load[h]>=applcableCapacity and self.load[h]:
                moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                if debugStrategy:
                    eprint('Harvester ',h,r,c, 'moving to nearestet depot via new path', moveCmds[h])

            elif self.slimes:
                moveCmds[h] = self.collectSlime(h,explored,self.load[h],None)
                if debugStrategy:
                    eprint('Harvester ',h,r,c, 'Collecting slime in new path', moveCmds[h])
            else:
                if self.load[h]:
                    moveCmds[h] = self.moveToNearestDepot(h,explored,self.load[h],depotbusy)
                    if debugStrategy:
                        eprint('No slime Moving to depot ',h,r,c, 'next move', moveCmds[h])
                else:
                    pass
                
        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if not self.load[h]:
                moveCmds[h] = self.moveAwayFromNearestDepot(h,explored,self.load[h],depotbusy)
                if debugStrategy:
                    eprint('Harvester ',h,r,c, 'Moving away', moveCmds[h])
                
        for h,(r,c) in enumerate(self.har):
            if moveCmds[h] is not None:
                continue
            if self.isNeighborBusy(h, moveCmds):
                continue
            if not self.load[h]:
                moveCmds[h] = self.wander(h, explored, self.load[h], depotbusy)
                if debugStrategy:
                    eprint('Wandering ',h,r,c, 'Moving away', moveCmds[h])
 

     
        self.sendMoves(moveCmds)

class AutoTester:

    def __init__(self,N,D,H,W,C,S,P):
        self.N = N
        self.D = D
        self.H = H
        self.wallP = int(W*10)
        self.C = C
        self.slimeP = int(S*10)
        self.P = P
        self.dc = [1,0,-1,0]
        self.dr = [0,1,0,-1]

        self.grid = None
        self.carry = [0]*H 
        self.entityC = [0]*H 
        self.entityR = [0]*H 
        self.depot = defaultdict(int)
        if debugGrid:
            eprint('AutoTester N=',self.N,'slimeP',self.slimeP,'wallP',self.wallP)

        while True:
            self.grid = [['.' for x in range(self.N)] for y in range(self.N)]
            emptyCells = N*N
            self.carry = [0]*H 
            self.entityC = [0]*H 
            self.entityR = [0]*H 
            #locDepots = [0]*D
            numSlime = 0;
            numHarvesters = 0;
            numDepots = 0;
            if debugGrid:
                eprint('Try random')

            def calcReachable():

                reachable = 0
                stack = []
                for r in range(self.N):
                    for c in range(self.N):
                        if self.grid[r][c] != WALL and self.grid[r][c] != DEPOT:
                            stack.append((r,c))
                            break
                    if stack:
                        break

                explored = [[False]*N for y in range(self.N)]
                explored[stack[0][0]][stack[0][1]] = True
                # run dfs
                while stack:
                    r,c = stack.pop()
                    reachable += 1
                    for d in range(4):
                        nr = r+self.dr[d]
                        nc = c+self.dc[d]
                        if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]==WALL or self.grid[nr][nc] == DEPOT:
                            continue
                        if explored[nr][nc]:
                            continue
                        explored[nr][nc] = True
                        stack.append((nr,nc))
                return reachable



            assert(calcReachable() == emptyCells)
            # place slime and walls
            for i in range(N):
                for k in range(N):
                    p = random.randint(0,9)
                    if p<self.slimeP:
                        self.grid[i][k] = SLIME
                        numSlime+=1
                    elif p<self.slimeP+self.wallP:
                        
                        self.grid[i][k] = WALL
                        emptyCells-=1
                        if calcReachable() != emptyCells:
                            self.grid[i][k] = EMPTY
                            emptyCells+=1
                            if debugGrid:
                                eprint('Cannot place wall');
                            continue
                    else:
                        self.grid[i][k] = EMPTY

            assert(calcReachable() == emptyCells)
            explored = [[False]*N for y in range(self.N)]
            for r in range(N):
                for c in range(N):
                    if self.grid[r][c] == SLIME:
                        explored[r][c] = True
                        for nr,nc in [(r-1,c-1),(r-1,c),(r+1,c),(r+1,c+1),(r,c+1),(r,c-1)]:
                            if nc<0 or nc>=self.N or nr<0 or nr>=self.N or self.grid[nr][nc]==WALL:
                                continue
                            explored[nr][nc] = True
                    elif self.grid[r][c] == WALL:
                        explored[r][c] = True
            
            assert(calcReachable() == emptyCells)
            available = [(r,c) for r in range(self.N) for c in range(self.N) if not explored[r][c]]            
            random.shuffle(available)
            for i in range(D):

                if not available:
                    break
                
                while available:
                    r,c = available.pop()
                    old = self.grid[r][c]
                    self.grid[r][c] = DEPOT;
                    emptyCells-=1
                    if calcReachable() != emptyCells:
                        eprint('Cannot place depot',len(available),calcReachable(),emptyCells);
                        self.grid[r][c] = old
                        emptyCells+=1
                        continue
                    #locDepots[numDepots] = r*N+c;
                    break
                
                numDepots+=1

            if not available:
                if debugGrid:
                    eprint('No available space')
                continue

            # Make sure everything is reachable by harvesters
            reachable = calcReachable()
            if reachable != emptyCells:
                if debugGrid:
                    eprint('Not reachable')
                continue # retry

            # place harvesters
            for i in range(H):
                r = random.randint(0, N-1);
                c = random.randint(0, N-1);
                while self.grid[r][c]!=EMPTY:
                    r = random.randint(0, N-1);
                    c = random.randint(0, N-1);
                    
                self.grid[r][c] = HARVESTER;
                self.carry[numHarvesters] = 0;
                self.entityC[numHarvesters] = c;
                self.entityR[numHarvesters] = r;
                numHarvesters+=1
            if reachable==emptyCells and numDepots>0 and numSlime>0 and numHarvesters>0:

                self.numStartDepots = numDepots;
                break;

        if debugGrid:
            eprint('Tester ready')
            eprint(self.grid)


    def setupHarvester(self):
        har = [(0,0)]*self.H
        for h in range(self.H):
            har[h] = [self.entityR[h],self.entityC[h]]
        return har
        
    def parseGrid(self,grid):
        for r in range(self.N):
            grid[r] = self.grid[r][:]
        

    def parseLoad(self):
        return self.carry[:]

    def pushCmd(self,cmd):
        assert(len(cmd) == self.H*2)
        if debug:
            cmdstr = ' '.join(cmd)
            #sys.stderr.write(cmdstr)
            eprint(cmdstr)

        cmd2 = cmd[:]
        while cmd2:
            move = cmd2.pop()
            h = int(cmd2.pop())

            if 'X' == move:
                continue # no action

            if 'U' == move:
                r = self.entityR[h]
                c = self.entityC[h]
                assert(r > 0)
                assert(self.grid[r][c] == HARVESTER)

                if self.grid[r-1][c] == SLIME:
                    self.carry[h] += 1
                    assert(self.carry[h] <= self.C)
                elif self.grid[r-1][c] == DEPOT:
                    self.depot[(r,c)] += 1
                    continue

                self.grid[r][c] = EMPTY
                r-=1                
                self.entityR[h] = r
                assert(self.grid[r][c] == EMPTY or self.grid[r][c] == SLIME)

                self.grid[r][c] = HARVESTER
                
            if 'D' == move:
                r = self.entityR[h]
                c = self.entityC[h]
                assert(r < (self.N-1))
                assert(self.grid[r][c] == HARVESTER)


                if self.grid[r+1][c] == SLIME:
                    self.carry[h] += 1
                    assert(self.carry[h] <= self.C)
                elif self.grid[r+1][c] == DEPOT:
                    self.depot[(r,c)] += 1
                    continue

                self.grid[r][c] = EMPTY
                r+=1
                self.entityR[h] = r
                assert(self.grid[r][c] == EMPTY or self.grid[r][c] == SLIME)
                self.grid[r][c] = HARVESTER

            if 'L' == move:
                r = self.entityR[h]
                c = self.entityC[h]
                assert(c > 0)
                assert(self.grid[r][c] == HARVESTER)

                if self.grid[r][c-1] == SLIME:
                    self.carry[h] += 1
                    assert(self.carry[h] <= self.C)
                elif self.grid[r][c-1] == DEPOT:
                    self.depot[(r,c)] += 1
                    continue

                self.grid[r][c] = EMPTY
                c-=1
                self.entityC[h] = c
                assert(self.grid[r][c] == EMPTY or self.grid[r][c] == SLIME)
                self.grid[r][c] = HARVESTER
 
 
            if 'R' == move:
                r = self.entityR[h]
                c = self.entityC[h]
                assert(c < (self.N-1))
                assert(self.grid[r][c] == HARVESTER)


                if self.grid[r][c+1] == SLIME:
                    self.carry[h] += 1
                    assert(self.carry[h] <= self.C)
                elif self.grid[r][c+1] == DEPOT:
                    self.depot[(r,c)] += 1
                    continue

                self.grid[r][c] = EMPTY
                c+=1
                self.entityC[h] = c
                assert(self.grid[r][c] == EMPTY or self.grid[r][c] == SLIME)
                self.grid[r][c] = HARVESTER
 


        #if debugGrid:
        #    eprint(self.grid)

    def calcScore(self):
        score = self.N*self.N
        for r in range(self.N):
            for c in range(self.N):
                if SLIME == self.grid[r][c]:
                    score -= 1
        for d in self.depot.values():
            score += d
        
        return score

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
        cmdstr = ' '.join(cmd)
        if debug:
            #sys.stderr.write(cmdstr)
            eprint(cmdstr)
        print(cmdstr)
        sys.stdout.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Test BioSlime')
    parser.add_argument('-N', '--ngrid', type=int, default=10, help='Grid size')
    parser.add_argument('-D', '--depot', type=int, default=1, help='Number of depots')
    parser.add_argument('-H', '--harvester', type=int, default=1, help='Number of Harvester')
    parser.add_argument('-W', '--wall', type=float, default=0.1, help='Wall probability')
    parser.add_argument('-C', '--capacity', type=int, default=1, help='Number of slimes the harvester can carry')
    parser.add_argument('-S', '--slimeS', type=float, default=0.1, help='Slime probability')
    parser.add_argument('-P', '--slimeP', type=float, default=0.1, help='Slime probability')
    parser.add_argument('-A', '--autotest', action='store_true', help='Run autotest')
    parser.add_argument('-T', '--tune', action='store_true', help='Try to tune parameter')
    parser.add_argument('-K', '--maxAllowedCapacity', type=int, default=MAXIMUM_ALLOWED_CAPACITY, help='Maximum capacity that is applicable')
    parser.add_argument('-M', '--harvesterPerDepot', type=int, default=MIN_HARVESTOR_PER_DEPOT, help='Maximum harvester per depot')

    args = parser.parse_args()
    if args.tune:

        result = [None]*31
        for N in range(10,31):
            result[N] = [None]*11
            for D in range(1,11):
                result[N][D] = [None]*21
                for H in range(1,21):
                    #bestscore = None
                    #bestparam = None

                    prototester = AutoTester(N,D,H,args.wall,args.capacity,args.slimeS,args.slimeP) 

                    result[N][D][H] = []
                    for maxAllowedCapacity in range(4,16):
                        for harvesterPerDepot in range(4,16):
                            MAXIMUM_ALLOWED_CAPACITY = maxAllowedCapacity
                            MIN_HARVESTOR_PER_DEPOT = harvesterPerDepot

                            tester = copy.deepcopy(prototester)

                            bsalg = BioSlime(tester)
                            bsalg.setup()

                            # Simulate 1000 turns
                            for turn in range(1000):
                                bsalg.run(turn)

                            print('Score',tester.calcScore())


                            result[N][D][H].append((tester.calcScore(), (maxAllowedCapacity,harvesterPerDepot)))

        print(result)

    elif args.autotest:
        MAXIMUM_ALLOWED_CAPACITY = args.maxAllowedCapacity
        MIN_HARVESTOR_PER_DEPOT = args.harvesterPerDepot
        # python3 BioSlime.py -N 30 -C 20 -D 8 -H 10 -S 0.5 -P 0.1 -W 0.1 -A
        tester = AutoTester(args.ngrid,args.depot,args.harvester,args.wall,args.capacity,args.slimeS,args.slimeP) 
        bsalg = BioSlime(tester)
        bsalg.setup()

        # Simulate 1000 turns
        for turn in range(1000):
            bsalg.run(turn)

        print('Score',tester.calcScore())
    else:
        MAXIMUM_ALLOWED_CAPACITY = args.maxAllowedCapacity
        MIN_HARVESTOR_PER_DEPOT = args.harvesterPerDepot

        tester = StdTester()
        bsalg = BioSlime(tester)
        bsalg.setup()

        # Simulate 1000 turns
        for turn in range(1000):
            bsalg.run(turn)



