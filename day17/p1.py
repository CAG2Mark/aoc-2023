from typing import List
from queue import PriorityQueue
from collections import defaultdict

# [cost, (newr, newc, disallowed dir)]
def neighbours(pos, visited, m, cur_cost):
    # extend 1 in each direction
    (row, col, skip) = pos

    ROWS = len(m)
    COLS = len(m[0])

    ret = []

    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    for dir in range(4):
        if skip != -1 and (dir == skip or dir % 2 == skip):
            continue
        
        (dr, dc) = DIRS[dir]

        cost = cur_cost
        for delta in range(1, 4):
            # Originally I stored all 4 possible directions in the state.
            # But after discussing our answers (credit to Fri3dNstuff) I 
            # realized I could just store two directions, horizontal and 
            # vertical, which reduces the state space by half.
            new_pos = (row + dr * delta, col + dc * delta, dir % 2)
            if not (0 <= new_pos[0] < ROWS and 0 <= new_pos[1] < COLS):
                break
            
            cost += m[new_pos[0]][new_pos[1]]

            if new_pos in visited:
                continue

            ret.append((cost, new_pos))

    return ret

def solve(inp: List[str]):
    # dijkstra
    q = PriorityQueue()

    m = [[int(x) for x in r] for r in inp]

    ROWS = len(m)
    COLS = len(m[0])

    # cost, (row, col, dir, disallowed direction)

    # 0 UP 1 RIGHT 2 DOWN 3 LEFT
    q.put((0, (0, 0, -1)))
    
    visited = set()

    ans = 100000

    prev = {}
    dists = defaultdict(lambda: float('inf'))
    dists[(0, 0, -1)] = 0

    while not q.empty():
        (cur_cost, pos) = q.get()

        if pos in visited:
            continue

        visited.add(pos)

        ns = neighbours(pos, visited, m, cur_cost)
        # print(pos, ns)
        for (new_dist, new_pos) in ns:
            if new_pos[0] == ROWS - 1 and new_pos[1] == COLS - 1:
                ans = min(new_dist, ans)
                # return ans
            if new_dist < dists[new_pos]:
                dists[new_pos] = new_dist
                q.put((new_dist, new_pos))
                prev[new_pos] = pos
    return ans
