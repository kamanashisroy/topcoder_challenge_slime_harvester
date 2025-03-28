
import time
import sys
from heapq import heappop,heappush,heapify

params = sys.argv[1:]
#eprint(params)
params = [int(x) for x in params]

bestParams = [None, None, None, None, None, None, None, None, None, None, [None, [None, 2, 5, 3, 3, 4, 2, 1, 1, 4, 7, 2, 4, 7, 5, 6, 5, 1, 5, 5, 5], [None, 5, 5, 2, 1, 5, 5, 4, 1, 6, 2, 2, 7, 2, 5, 3, 1, 3, 3, 4, 3], [None, 4, 4, 5, 2, 5, 4, 5, 4, 5, 4, 7, 2, 3, 1, 2, 4, 5, 5, 1, 1], [None, 4, 3, 1, 2, 4, 2, 3, 5, 1, 2, 4, 1, 4, 3, 4, 4, 5, 3, 4, 3], [None, 3, 5, 1, 1, 3, 1, 1, 3, 1, 4, 1, 2, 1, 4, 2, 1, 2, 1, 3, 2], [None, 3, 4, 3, 2, 1, 3, 3, 3, 4, 2, 3, 1, 5, 5, 3, 2, 2, 1, 3, 3], [None, 4, 1, 2, 5, 1, 4, 1, 5, 5, 4, 1, 2, 2, 2, 5, 3, 5, 5, 5, 2], [None, 5, 5, 2, 1, 4, 4, 2, 3, 5, 5, 1, 5, 3, 1, 5, 5, 2, 4, 5, 2], [None, 5, 1, 3, 1, 5, 4, 5, 5, 2, 3, 1, 1, 3, 5, 2, 2, 3, 3, 5, 2], [None, 3, 5, 1, 2, 2, 1, 5, 2, 5, 5, 5, 2, 3, 2, 1, 1, 5, 3, 1, 3]], [None, [None, 4, 1, 1, 1, 1, 2, 1, 6, 2, 4, 7, 5, 2, 5, 5, 4, 2, 5, 1, 5], [None, 3, 5, 3, 4, 4, 5, 2, 3, 7, 3, 4, 7, 6, 6, 2, 1, 1, 2, 4, 1], [None, 1, 2, 2, 3, 2, 5, 2, 2, 1, 7, 2, 5, 6, 3, 3, 3, 3, 3, 1, 1], [None, 1, 5, 3, 4, 2, 1, 1, 4, 1, 5, 3, 7, 5, 5, 1, 4, 5, 4, 2, 5], [None, 2, 3, 5, 5, 4, 2, 1, 4, 1, 2, 3, 2, 1, 5, 4, 1, 5, 3, 3, 3], [None, 1, 4, 3, 2, 1, 2, 3, 5, 3, 1, 2, 5, 3, 2, 2, 4, 3, 3, 3, 2], [None, 2, 5, 2, 1, 2, 3, 4, 2, 3, 4, 4, 3, 1, 4, 1, 2, 4, 5, 5, 3], [None, 3, 5, 1, 3, 1, 5, 2, 3, 4, 4, 3, 2, 4, 4, 3, 1, 5, 4, 3, 5], [None, 2, 5, 5, 3, 3, 5, 5, 4, 4, 5, 5, 3, 3, 5, 5, 2, 2, 2, 1, 5], [None, 3, 4, 4, 5, 4, 3, 3, 4, 5, 5, 5, 2, 1, 5, 3, 5, 2, 1, 4, 3]], [None, [None, 4, 4, 4, 3, 2, 3, 5, 2, 1, 4, 2, 3, 3, 1, 2, 3, 2, 2, 1, 5], [None, 1, 4, 2, 5, 1, 3, 2, 3, 1, 4, 6, 3, 1, 1, 1, 1, 1, 4, 1, 2], [None, 3, 2, 4, 1, 2, 3, 4, 6, 1, 2, 3, 1, 1, 3, 2, 1, 4, 5, 1, 4], [None, 3, 4, 3, 1, 2, 5, 3, 2, 1, 1, 1, 4, 5, 1, 5, 5, 3, 5, 1, 1], [None, 4, 1, 5, 3, 4, 3, 2, 4, 1, 5, 1, 3, 3, 2, 2, 4, 1, 3, 1, 2], [None, 2, 2, 1, 3, 2, 5, 3, 4, 1, 3, 2, 1, 1, 1, 2, 3, 3, 1, 5, 4], [None, 2, 3, 5, 2, 1, 4, 2, 1, 2, 2, 1, 5, 2, 2, 2, 1, 1, 3, 3, 5], [None, 4, 3, 4, 1, 5, 5, 1, 4, 1, 3, 2, 1, 3, 5, 1, 5, 3, 1, 2, 3], [None, 1, 5, 3, 4, 1, 3, 3, 2, 5, 3, 1, 1, 2, 3, 4, 3, 2, 5, 4, 5], [None, 3, 5, 3, 2, 3, 2, 2, 1, 2, 4, 3, 1, 4, 1, 4, 5, 3, 2, 5, 5]], [None, [None, 1, 3, 1, 4, 5, 3, 1, 2, 3, 1, 1, 1, 7, 3, 6, 5, 5, 3, 2, 1], [None, 2, 3, 5, 3, 4, 5, 3, 7, 7, 4, 4, 3, 4, 1, 5, 2, 4, 2, 5, 3], [None, 5, 2, 5, 5, 4, 3, 1, 1, 2, 7, 2, 2, 4, 7, 6, 5, 4, 2, 3, 3], [None, 2, 1, 4, 4, 2, 1, 5, 1, 2, 4, 3, 4, 1, 6, 6, 2, 4, 5, 1, 5], [None, 2, 4, 5, 5, 2, 2, 1, 3, 2, 4, 5, 3, 2, 5, 1, 1, 1, 2, 4, 5], [None, 1, 1, 1, 5, 4, 1, 5, 1, 2, 3, 2, 2, 3, 1, 2, 5, 1, 2, 4, 3], [None, 4, 1, 5, 1, 4, 4, 2, 3, 1, 1, 1, 4, 5, 2, 5, 1, 4, 1, 4, 3], [None, 1, 4, 1, 1, 1, 4, 3, 4, 1, 2, 4, 4, 2, 4, 2, 3, 2, 1, 2, 4], [None, 1, 1, 1, 2, 1, 1, 5, 3, 2, 1, 1, 2, 2, 3, 2, 2, 5, 2, 5, 2], [None, 4, 1, 5, 1, 2, 5, 4, 1, 3, 2, 5, 4, 3, 4, 5, 1, 5, 3, 5, 2]], [None, [None, 1, 4, 5, 4, 2, 1, 1, 1, 1, 7, 1, 6, 4, 1, 1, 4, 5, 2, 3, 4], [None, 4, 1, 4, 5, 3, 1, 1, 2, 3, 1, 1, 1, 2, 3, 2, 5, 1, 1, 5, 2], [None, 2, 3, 4, 3, 1, 2, 3, 1, 1, 1, 7, 2, 7, 7, 5, 2, 2, 5, 5, 4], [None, 1, 2, 3, 2, 4, 5, 2, 3, 4, 1, 2, 6, 2, 4, 3, 3, 1, 1, 4, 4], [None, 4, 4, 4, 2, 1, 4, 1, 1, 3, 3, 1, 4, 2, 4, 4, 1, 5, 1, 4, 4], [None, 4, 2, 3, 5, 3, 4, 3, 1, 1, 1, 3, 4, 1, 2, 5, 3, 1, 3, 4, 3], [None, 5, 5, 3, 5, 5, 5, 4, 1, 5, 5, 4, 3, 3, 3, 1, 3, 1, 1, 3, 5], [None, 1, 3, 1, 5, 5, 1, 1, 3, 3, 1, 4, 4, 2, 4, 3, 3, 5, 3, 5, 4], [None, 1, 2, 4, 5, 2, 1, 2, 3, 1, 3, 4, 5, 3, 5, 2, 4, 2, 3, 5, 3], [None, 5, 3, 4, 4, 2, 1, 4, 1, 1, 2, 4, 2, 3, 4, 4, 1, 5, 3, 1, 1]], [None, [None, 1, 2, 3, 5, 5, 3, 3, 3, 2, 3, 6, 5, 6, 5, 3, 1, 5, 2, 3, 3], [None, 3, 1, 5, 4, 1, 1, 1, 4, 7, 5, 1, 7, 1, 2, 7, 5, 2, 5, 4, 3], [None, 1, 5, 5, 4, 4, 1, 1, 3, 1, 4, 2, 1, 4, 2, 2, 5, 4, 1, 5, 5], [None, 1, 5, 3, 3, 3, 3, 5, 7, 2, 5, 4, 4, 2, 1, 6, 2, 1, 4, 5, 2], [None, 1, 4, 4, 4, 2, 2, 3, 4, 5, 1, 3, 3, 5, 1, 5, 1, 1, 5, 3, 5], [None, 1, 3, 2, 4, 3, 2, 5, 3, 5, 5, 2, 1, 1, 2, 5, 5, 5, 3, 5, 1], [None, 1, 1, 1, 5, 2, 3, 4, 5, 3, 4, 5, 4, 1, 5, 1, 2, 4, 4, 5, 5], [None, 1, 3, 2, 1, 4, 4, 5, 3, 5, 4, 1, 4, 5, 1, 5, 5, 5, 5, 4, 1], [None, 1, 4, 5, 5, 2, 3, 1, 1, 5, 5, 2, 3, 5, 5, 2, 5, 3, 1, 4, 5], [None, 1, 5, 5, 1, 4, 4, 2, 4, 1, 3, 1, 1, 3, 1, 3, 5, 5, 3, 1, 2]], [None, [None, 1, 5, 4, 3, 5, 2, 2, 6, 3, 1, 1, 7, 5, 1, 4, 1, 1, 4, 1, 3], [None, 2, 5, 2, 5, 4, 2, 1, 5, 1, 3, 1, 2, 4, 6, 2, 5, 4, 3, 2, 2], [None, 3, 2, 4, 5, 3, 3, 5, 6, 4, 1, 1, 7, 5, 4, 1, 3, 5, 5, 5, 5], [None, 2, 3, 4, 4, 5, 1, 4, 2, 6, 3, 4, 4, 7, 3, 2, 3, 2, 5, 4, 2], [None, 2, 4, 2, 4, 2, 5, 1, 5, 3, 1, 3, 4, 5, 1, 3, 4, 4, 3, 2, 4], [None, 1, 3, 2, 4, 1, 4, 3, 5, 3, 1, 4, 5, 4, 1, 3, 4, 2, 4, 3, 2], [None, 5, 4, 2, 1, 5, 5, 2, 2, 1, 5, 2, 3, 3, 3, 5, 3, 4, 5, 3, 4], [None, 4, 5, 3, 2, 3, 5, 2, 3, 1, 4, 4, 3, 2, 4, 5, 2, 1, 2, 1, 3], [None, 5, 4, 5, 2, 4, 3, 4, 1, 2, 5, 2, 2, 5, 4, 5, 2, 4, 2, 2, 2], [None, 4, 5, 3, 5, 5, 5, 1, 1, 1, 3, 1, 1, 4, 4, 1, 1, 3, 5, 5, 3]], [None, [None, 5, 1, 5, 5, 3, 3, 4, 2, 7, 4, 1, 1, 3, 3, 7, 1, 2, 5, 4, 5], [None, 5, 3, 4, 3, 1, 5, 1, 3, 1, 2, 2, 6, 5, 3, 1, 4, 4, 1, 5, 5], [None, 4, 1, 5, 2, 5, 4, 3, 4, 1, 7, 5, 7, 7, 1, 6, 1, 5, 3, 5, 5], [None, 5, 4, 3, 3, 5, 3, 5, 6, 4, 1, 2, 4, 3, 7, 5, 4, 1, 2, 3, 3], [None, 5, 1, 1, 1, 4, 5, 4, 5, 4, 3, 4, 1, 1, 5, 5, 4, 3, 1, 1, 4], [None, 2, 4, 2, 4, 1, 5, 2, 1, 2, 4, 2, 1, 1, 5, 4, 2, 1, 3, 3, 2], [None, 4, 5, 2, 2, 5, 5, 3, 1, 2, 1, 1, 1, 1, 2, 5, 5, 5, 5, 2, 4], [None, 4, 3, 5, 4, 3, 1, 3, 1, 1, 3, 3, 4, 2, 5, 5, 4, 5, 4, 5, 3], [None, 5, 2, 4, 1, 3, 5, 4, 4, 4, 5, 4, 2, 5, 5, 5, 2, 3, 5, 3, 1], [None, 4, 5, 3, 3, 1, 4, 5, 5, 4, 4, 3, 3, 2, 4, 4, 1, 2, 5, 1, 1]], [None, [None, 3, 4, 4, 1, 3, 1, 2, 2, 4, 1, 1, 4, 7, 3, 7, 5, 5, 1, 2, 5], [None, 2, 5, 4, 4, 2, 1, 5, 3, 2, 5, 6, 4, 4, 6, 3, 2, 5, 1, 5, 5], [None, 2, 5, 1, 5, 1, 1, 1, 4, 2, 5, 6, 3, 3, 1, 4, 3, 3, 2, 3, 1], [None, 5, 5, 5, 1, 1, 5, 5, 4, 5, 6, 5, 4, 5, 5, 4, 1, 4, 5, 3, 1], [None, 4, 2, 2, 4, 3, 4, 2, 3, 5, 3, 5, 2, 5, 4, 1, 4, 3, 2, 1, 1], [None, 1, 4, 1, 3, 3, 2, 3, 4, 1, 3, 2, 3, 2, 3, 1, 2, 1, 1, 1, 1], [None, 4, 4, 4, 1, 4, 1, 4, 1, 4, 2, 3, 2, 4, 4, 4, 1, 4, 1, 2, 1], [None, 2, 1, 4, 4, 3, 3, 4, 4, 4, 1, 1, 4, 2, 4, 3, 1, 4, 3, 2, 4], [None, 3, 2, 1, 1, 2, 1, 1, 4, 1, 4, 1, 1, 4, 3, 4, 4, 3, 1, 1, 1], [None, 1, 1, 3, 1, 2, 3, 1, 1, 2, 1, 2, 3, 1, 3, 2, 1, 3, 2, 3, 2]], [None, [None, 1, 3, 3, 4, 4, 4, 3, 4, 5, 5, 7, 2, 2, 7, 5, 3, 2, 2, 3, 1], [None, 2, 1, 4, 4, 3, 3, 4, 3, 7, 6, 7, 1, 1, 7, 1, 3, 1, 1, 4, 3], [None, 1, 3, 4, 3, 3, 4, 3, 3, 1, 7, 6, 5, 1, 1, 2, 1, 3, 2, 2, 1], [None, 3, 4, 1, 1, 1, 4, 4, 7, 5, 2, 1, 6, 4, 1, 6, 4, 2, 2, 4, 1], [None, 1, 1, 4, 3, 3, 4, 4, 4, 4, 3, 3, 4, 2, 2, 2, 4, 3, 4, 4, 3], [None, 2, 4, 4, 4, 3, 4, 1, 2, 2, 1, 2, 4, 4, 2, 2, 2, 2, 4, 4, 4], [None, 2, 4, 3, 4, 4, 4, 4, 1, 1, 3, 4, 1, 4, 3, 4, 2, 3, 2, 4, 3], [None, 2, 2, 4, 3, 3, 4, 2, 1, 2, 1, 2, 1, 2, 3, 4, 4, 4, 2, 2, 1], [None, 2, 4, 4, 2, 2, 4, 2, 3, 4, 2, 3, 4, 2, 2, 3, 4, 2, 1, 3, 2], [None, 2, 4, 4, 1, 4, 4, 4, 3, 1, 4, 2, 1, 4, 4, 3, 4, 2, 2, 4, 1]], [None, [None, 1, 2, 4, 3, 3, 4, 4, 4, 4, 4, 2, 4, 4, 3, 4, 4, 1, 2, 2, 4], [None, 1, 3, 3, 4, 4, 2, 4, 4, 4, 3, 1, 4, 1, 4, 2, 3, 2, 4, 4, 3], [None, 3, 2, 1, 4, 3, 4, 4, 4, 1, 2, 3, 3, 3, 2, 4, 4, 3, 4, 2, 3], [None, 1, 2, 4, 3, 4, 4, 1, 4, 1, 4, 4, 4, 3, 3, 3, 3, 1, 3, 3, 4], [None, 2, 1, 4, 4, 4, 4, 3, 4, 3, 1, 4, 4, 4, 3, 4, 4, 1, 2, 4, 3], [None, 3, 4, 3, 4, 4, 4, 4, 1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 4, 2, 4], [None, 1, 1, 4, 3, 3, 4, 1, 1, 2, 4, 3, 4, 4, 4, 4, 4, 3, 2, 3, 4], [None, 2, 1, 2, 4, 3, 4, 2, 1, 3, 4, 4, 4, 4, 4, 3, 3, 3, 3, 4, 3], [None, 1, 1, 3, 3, 3, 4, 2, 4, 4, 4, 4, 3, 2, 4, 4, 3, 2, 4, 3, 4], [None, 4, 1, 4, 4, 1, 4, 4, 3, 3, 3, 3, 3, 3, 4, 3, 2, 4, 3, 4, 4]], [None, [None, 1, 2, 1, 3, 2, 1, 2, 2, 2, 4, 3, 2, 3, 2, 3, 3, 4, 1, 3, 3], [None, 2, 2, 2, 1, 4, 4, 3, 4, 3, 4, 4, 1, 4, 2, 1, 3, 1, 1, 1, 4], [None, 1, 1, 1, 4, 1, 2, 1, 3, 1, 3, 3, 3, 2, 2, 2, 1, 4, 3, 3, 3], [None, 3, 1, 1, 2, 4, 4, 3, 3, 4, 4, 3, 1, 4, 3, 3, 1, 4, 4, 1, 2], [None, 4, 1, 1, 4, 1, 4, 4, 4, 1, 1, 3, 1, 4, 2, 4, 2, 4, 4, 1, 2], [None, 1, 4, 3, 3, 4, 3, 4, 4, 4, 1, 2, 2, 4, 2, 2, 4, 4, 4, 3, 4], [None, 4, 4, 1, 4, 3, 2, 4, 4, 1, 4, 3, 4, 1, 4, 4, 2, 4, 3, 2, 3], [None, 4, 3, 3, 3, 1, 4, 4, 4, 4, 1, 3, 1, 2, 3, 3, 4, 4, 2, 1, 4], [None, 1, 1, 4, 1, 1, 2, 4, 4, 1, 1, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4], [None, 1, 2, 3, 4, 3, 3, 4, 3, 3, 4, 3, 3, 4, 2, 3, 4, 4, 3, 4, 3]], [None, [None, 1, 1, 2, 4, 2, 2, 4, 4, 3, 4, 4, 4, 3, 2, 4, 3, 1, 4, 2, 2], [None, 1, 3, 1, 1, 2, 1, 3, 4, 3, 3, 1, 4, 2, 3, 1, 3, 1, 2, 4, 4], [None, 1, 4, 2, 3, 3, 4, 4, 3, 4, 1, 1, 2, 1, 2, 1, 2, 3, 3, 1, 4], [None, 4, 1, 3, 4, 4, 2, 1, 4, 1, 1, 1, 2, 1, 1, 1, 3, 3, 3, 1, 1], [None, 1, 3, 1, 1, 3, 3, 4, 2, 2, 4, 1, 1, 3, 2, 4, 1, 4, 3, 4, 2], [None, 1, 2, 3, 3, 3, 3, 4, 3, 3, 1, 1, 1, 4, 4, 1, 4, 1, 4, 3, 2], [None, 4, 1, 3, 4, 3, 2, 3, 4, 2, 1, 3, 4, 1, 3, 4, 2, 3, 4, 4, 2], [None, 1, 3, 4, 2, 2, 4, 4, 3, 4, 2, 1, 2, 2, 4, 4, 4, 1, 4, 2, 4], [None, 1, 1, 2, 3, 3, 4, 1, 4, 3, 1, 2, 4, 2, 3, 3, 4, 2, 3, 4, 4], [None, 1, 3, 4, 3, 3, 4, 4, 3, 4, 3, 4, 2, 3, 3, 2, 4, 4, 2, 4, 3]], [None, [None, 1, 3, 3, 2, 2, 4, 3, 3, 2, 3, 2, 4, 3, 4, 3, 4, 4, 3, 3, 4], [None, 1, 4, 2, 4, 4, 4, 3, 4, 1, 2, 3, 4, 3, 4, 4, 2, 3, 4, 3, 4], [None, 2, 1, 4, 4, 4, 3, 3, 4, 1, 2, 2, 1, 4, 1, 1, 1, 2, 1, 2, 2], [None, 3, 1, 3, 3, 3, 4, 4, 3, 4, 4, 4, 3, 2, 2, 4, 1, 3, 2, 4, 1], [None, 1, 4, 3, 4, 3, 4, 4, 3, 4, 1, 4, 4, 3, 3, 3, 4, 4, 4, 4, 3], [None, 3, 2, 4, 2, 3, 4, 4, 3, 4, 4, 1, 3, 1, 2, 2, 2, 4, 3, 3, 4], [None, 3, 2, 4, 3, 3, 4, 4, 4, 4, 2, 2, 4, 4, 4, 2, 1, 3, 4, 3, 2], [None, 3, 4, 3, 3, 3, 4, 4, 3, 1, 1, 2, 1, 2, 1, 1, 4, 2, 4, 4, 4], [None, 1, 1, 3, 4, 3, 4, 4, 3, 3, 3, 3, 1, 2, 3, 4, 4, 3, 2, 3, 4], [None, 3, 3, 3, 4, 4, 4, 2, 1, 4, 1, 1, 3, 4, 2, 1, 3, 2, 4, 3, 4]], [None, [None, 3, 3, 1, 1, 4, 4, 3, 2, 2, 4, 4, 3, 4, 3, 2, 4, 3, 3, 4, 4], [None, 1, 4, 3, 4, 2, 3, 1, 3, 4, 3, 3, 3, 4, 4, 4, 4, 4, 4, 3, 1], [None, 3, 1, 2, 1, 3, 3, 3, 2, 4, 3, 4, 3, 3, 2, 4, 2, 4, 4, 1, 4], [None, 4, 2, 4, 1, 4, 2, 2, 3, 3, 4, 3, 3, 4, 4, 4, 4, 1, 1, 4, 4], [None, 4, 4, 2, 4, 3, 4, 2, 4, 3, 2, 2, 2, 1, 1, 1, 1, 1, 3, 1, 2], [None, 4, 4, 4, 4, 1, 2, 2, 4, 4, 2, 3, 1, 4, 4, 1, 2, 1, 2, 1, 2], [None, 3, 2, 2, 1, 1, 4, 2, 4, 4, 3, 3, 3, 2, 2, 4, 1, 3, 1, 2, 3], [None, 4, 3, 3, 4, 1, 3, 4, 4, 1, 4, 2, 4, 2, 1, 2, 1, 3, 1, 4, 3], [None, 3, 2, 2, 1, 2, 3, 2, 3, 4, 4, 2, 2, 2, 2, 4, 4, 4, 3, 4, 3], [None, 1, 4, 4, 2, 2, 4, 3, 3, 4, 2, 2, 4, 1, 3, 4, 4, 4, 3, 3, 2]], [None, [None, 2, 2, 2, 1, 4, 3, 3, 4, 1, 2, 2, 1, 4, 3, 4, 3, 4, 1, 1, 4], [None, 3, 3, 2, 4, 2, 3, 2, 2, 2, 3, 1, 3, 2, 3, 1, 1, 3, 2, 2, 2], [None, 3, 4, 3, 2, 1, 2, 2, 4, 3, 1, 1, 2, 1, 2, 3, 4, 4, 2, 1, 2], [None, 1, 4, 3, 1, 2, 2, 1, 1, 3, 1, 2, 4, 4, 3, 1, 4, 4, 2, 4, 2], [None, 3, 2, 1, 3, 2, 3, 4, 1, 3, 1, 1, 3, 1, 1, 1, 2, 4, 3, 4, 2], [None, 1, 1, 1, 1, 1, 2, 1, 2, 4, 2, 2, 4, 3, 3, 4, 1, 4, 4, 4, 3], [None, 1, 3, 1, 1, 1, 3, 4, 3, 4, 4, 1, 3, 4, 1, 2, 3, 3, 4, 2, 3], [None, 3, 2, 4, 1, 1, 1, 2, 3, 3, 1, 4, 3, 2, 2, 2, 3, 1, 1, 2, 1], [None, 3, 4, 4, 1, 3, 3, 2, 4, 1, 3, 1, 1, 1, 1, 3, 4, 4, 2, 3, 1], [None, 1, 4, 4, 4, 4, 4, 1, 1, 2, 1, 3, 1, 4, 1, 3, 2, 3, 4, 2, 3]], [None, [None, 1, 2, 4, 4, 3, 2, 4, 3, 2, 4, 4, 4, 4, 3, 3, 2, 4, 4, 2, 4], [None, 3, 1, 4, 2, 4, 4, 4, 2, 4, 4, 3, 2, 4, 4, 4, 3, 4, 4, 2, 3], [None, 4, 1, 4, 4, 3, 2, 4, 2, 3, 3, 2, 2, 3, 4, 2, 3, 4, 1, 4, 1], [None, 4, 3, 1, 4, 4, 3, 1, 2, 4, 4, 2, 1, 4, 3, 2, 4, 2, 2, 3, 1], [None, 4, 2, 3, 2, 4, 2, 4, 3, 2, 2, 4, 3, 2, 2, 2, 1, 4, 1, 1, 4], [None, 2, 1, 2, 3, 3, 4, 3, 2, 4, 4, 4, 4, 2, 1, 1, 4, 4, 1, 2, 1], [None, 2, 1, 2, 4, 4, 3, 2, 4, 2, 4, 4, 4, 4, 2, 1, 1, 3, 1, 2, 4], [None, 3, 4, 4, 4, 2, 3, 4, 4, 2, 3, 2, 4, 2, 4, 4, 1, 4, 1, 1, 4], [None, 1, 3, 3, 3, 4, 3, 4, 4, 2, 4, 4, 4, 1, 1, 1, 3, 2, 1, 3, 4], [None, 4, 4, 3, 3, 4, 3, 4, 4, 4, 2, 1, 4, 2, 1, 1, 1, 3, 4, 3, 1]], [None, [None, 4, 1, 2, 2, 3, 1, 4, 4, 3, 4, 4, 4, 3, 4, 3, 3, 3, 1, 3, 3], [None, 2, 1, 1, 4, 3, 4, 3, 3, 3, 4, 2, 4, 4, 4, 4, 4, 1, 4, 3, 3], [None, 1, 2, 2, 1, 2, 3, 2, 4, 3, 3, 3, 3, 3, 1, 1, 3, 1, 1, 2, 1], [None, 2, 1, 1, 2, 3, 2, 3, 4, 2, 2, 3, 4, 3, 2, 1, 3, 4, 1, 1, 1], [None, 4, 1, 1, 3, 3, 3, 1, 1, 4, 2, 2, 2, 4, 4, 2, 1, 4, 3, 3, 2], [None, 1, 2, 1, 2, 4, 4, 3, 3, 3, 3, 3, 4, 2, 1, 3, 3, 4, 1, 1, 4], [None, 2, 3, 3, 2, 1, 4, 1, 2, 3, 4, 3, 3, 3, 3, 4, 1, 1, 2, 1, 3], [None, 1, 1, 3, 4, 3, 3, 1, 3, 4, 4, 4, 4, 4, 1, 1, 2, 2, 1, 4, 3], [None, 3, 2, 1, 4, 4, 3, 1, 2, 4, 3, 3, 3, 2, 4, 4, 1, 4, 1, 2, 3], [None, 3, 1, 1, 1, 3, 4, 4, 2, 2, 3, 4, 3, 1, 1, 4, 3, 1, 1, 4, 1]], [None, [None, 4, 1, 3, 2, 3, 2, 2, 3, 3, 3, 4, 2, 4, 2, 2, 3, 2, 4, 4, 2], [None, 1, 2, 2, 3, 1, 2, 2, 2, 3, 2, 3, 4, 4, 2, 3, 4, 3, 2, 2, 4], [None, 1, 3, 2, 2, 1, 4, 3, 4, 2, 2, 2, 4, 4, 3, 4, 2, 2, 1, 3, 4], [None, 4, 2, 2, 3, 2, 3, 3, 1, 3, 2, 2, 2, 4, 4, 4, 3, 2, 3, 4, 4], [None, 3, 3, 1, 1, 4, 4, 3, 2, 2, 3, 3, 3, 4, 4, 4, 2, 2, 4, 4, 2], [None, 4, 2, 1, 2, 4, 2, 1, 2, 1, 2, 2, 4, 1, 4, 3, 1, 3, 4, 1, 1], [None, 3, 2, 1, 3, 4, 4, 2, 4, 4, 3, 4, 4, 4, 4, 4, 4, 1, 4, 1, 2], [None, 3, 1, 1, 3, 3, 3, 3, 4, 1, 4, 4, 4, 2, 4, 4, 2, 4, 4, 1, 2], [None, 2, 1, 1, 1, 4, 3, 2, 3, 3, 2, 2, 2, 1, 4, 3, 3, 2, 1, 4, 1], [None, 2, 3, 3, 4, 2, 3, 4, 1, 3, 4, 2, 4, 4, 2, 2, 4, 1, 1, 3, 1]], [None, [None, 4, 3, 3, 3, 3, 3, 3, 4, 4, 3, 3, 4, 4, 3, 3, 2, 3, 4, 2, 2], [None, 2, 4, 1, 4, 3, 1, 3, 3, 4, 3, 4, 4, 4, 4, 4, 3, 3, 4, 2, 4], [None, 4, 4, 2, 4, 1, 3, 3, 4, 4, 3, 3, 3, 4, 4, 3, 3, 3, 4, 3, 4], [None, 3, 3, 3, 3, 3, 4, 2, 4, 1, 4, 3, 3, 3, 4, 4, 4, 2, 1, 4, 4], [None, 4, 1, 3, 3, 4, 2, 4, 4, 3, 2, 4, 4, 3, 2, 4, 3, 3, 4, 4, 1], [None, 1, 3, 1, 2, 4, 4, 3, 3, 4, 4, 3, 3, 4, 2, 4, 3, 2, 1, 1, 1], [None, 1, 3, 3, 1, 4, 3, 3, 3, 3, 3, 2, 4, 4, 4, 4, 1, 1, 1, 1, 2], [None, 1, 3, 2, 3, 1, 3, 1, 3, 3, 4, 3, 4, 3, 4, 1, 4, 4, 1, 1, 1], [None, 1, 3, 4, 4, 3, 3, 3, 2, 4, 4, 4, 4, 4, 3, 1, 3, 1, 1, 1, 1], [None, 1, 1, 4, 4, 3, 4, 3, 4, 2, 2, 4, 4, 4, 4, 2, 4, 4, 4, 1, 1]], [None, [None, 2, 3, 1, 3, 4, 3, 3, 2, 4, 1, 2, 3, 4, 3, 3, 4, 4, 2, 2, 4], [None, 1, 3, 1, 1, 4, 2, 2, 4, 3, 3, 4, 3, 2, 4, 4, 3, 2, 3, 2, 2], [None, 2, 1, 3, 1, 3, 4, 3, 2, 1, 4, 3, 3, 3, 4, 4, 4, 3, 3, 3, 2], [None, 3, 1, 4, 3, 3, 2, 4, 4, 2, 2, 3, 4, 3, 4, 3, 2, 4, 3, 2, 4], [None, 3, 2, 4, 1, 1, 4, 3, 4, 2, 4, 3, 4, 4, 3, 4, 2, 4, 2, 2, 2], [None, 3, 1, 1, 2, 2, 4, 1, 3, 3, 4, 1, 3, 2, 1, 2, 2, 4, 4, 4, 2], [None, 4, 2, 1, 4, 1, 3, 3, 4, 2, 2, 3, 4, 4, 4, 4, 2, 4, 4, 1, 3], [None, 4, 2, 4, 3, 3, 4, 2, 4, 2, 2, 4, 4, 3, 1, 1, 3, 4, 3, 3, 2], [None, 1, 3, 4, 3, 3, 4, 3, 1, 4, 3, 3, 3, 3, 3, 4, 3, 3, 3, 3, 2], [None, 4, 3, 2, 2, 4, 2, 4, 2, 2, 4, 4, 3, 3, 4, 4, 2, 3, 2, 3, 2]]]




if len(params) < 2:
    if len(params) < 1:
        params = [3,800]
    else:
        params.append(800)

debug = False
debugStrategy=False
debugMove = False
debugCalStrategy=True
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

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

    def autoParam(self):

        if self.N < len(bestParams) and bestParams[self.N] is not None:
            if self.D < len(bestParams[self.N]) and bestParams[self.N][self.D] is not None:
                if self.H < len(bestParams[self.N][self.D]) and bestParams[self.N][self.D][self.H] is not None:
                    self.PARAM_DIV = bestParams[self.N][self.D][self.H] 
                    if debugCalStrategy:
                        eprint('Found auto param', self.PARAM_DIV)

        if debugCalStrategy:
            eprint('Auto param', self.PARAM_DIV)


    def calculateScore(self, numSlimes):
        
        totalScore = self.N*self.N
        totalScore -= numSlimes
        for d in range(self.D):
            if self.depotbad[d]:
                continue
            totalScore += self.depotscore[d]
        return totalScore

    def calculateApplicableCapacity(self, turn, slimes):

        curNumSlimes = len(slimes)

        if 0 == turn:
            self.prevScore = self.calculateScore(curNumSlimes)
            self.prevNumSlimes = len(slimes)
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
        self.prevNumSlimes = len(slimes)

        if debugCalStrategy:
            eprint(turn, 'Applicable capacity', self.applcableCapacity)
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
        self.calStrategy = CalibrationStrategy(self.N,self.C,self.H,params[0],params[1])

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
        self.depotscore = [0]*self.D
        self.calStrategy.setupDepot(self.depotbad,self.depotscore)

        self.calStrategy.autoParam()

        # This path will be useful to return to depot
        self.buildShortestPathFromDepot()

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
            return self.shortestPathAB(begr,begc,dr,dc,limit,explored,myload)
        return None



    def shortestPathToSlime(self,h,limit,explored,myload):
        begr,begc = self.har[h]
        # we need to return to depot after grabbing slime
        depotidx = self.depotAffinity[h]
        if depotidx is None:
            depotidx = 0
        dr,dc = self.depots[depotidx]
        
        hp = []
        for i,(sr,sc) in enumerate(self.slimes):
            hp.append((self.manhatdist(sr,sc,begr,begc)+self.manhatdist(sr,sc,dr,dc),i))
        
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

        self.turn = turn
        explored = set()

        # find the slimes and nearest harvestors
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
                
        #self.slimeSubGrids = self.buildSlimeSubGrids(slimes)

        applcableCapacity = self.calStrategy.calculateApplicableCapacity(turn, self.slimes)
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
            if self.load[h]>=applcableCapacity:
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
            #if self.isNeighborBusy(h, moveCmds):
            #    continue
            if not self.load[h]:
                moveCmds[h] = self.wander(h, explored, self.load[h], depotbusy)
                if debugStrategy:
                    eprint('Wandering ',h,r,c, 'Moving away', moveCmds[h])
 

     
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
        cmdstr = ' '.join(cmd)
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



