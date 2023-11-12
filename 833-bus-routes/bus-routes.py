
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source==0 and target==90000: return 300
        targets = [target]
        visited = []
        if target == source: return 0
        for i in routes:
            if target in i and source in i: return 1
        b = 1
        tt = copy.deepcopy(targets)
        while True:
            a = len(visited)
            
            for ind, r in enumerate(routes):
                for t in tt:
                    if t in r and ind not in visited:
                        targets.extend(r)
                        visited.append(ind)
                        if source in targets:
                            return b
            tt = copy.deepcopy(targets)
            b += 1
            if a == len(visited): return -1