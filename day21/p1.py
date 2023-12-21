from typing import List
from collections import deque

def solve(inp: List[str]):
    ROWS = len(inp)
    COLS = len(inp[0])

    r = -1
    c = -1

    for i, ln in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch == 'S':
                r = i
                c = j
                break
    
    DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    

    Q = deque()
    Q.append((0, r, c))
    SEEN = set()
    SEEN.add((r, c)) 
    cnt = 0
    
    STEPS = 64

    while Q:
        (it, r, c) = Q.popleft()

        # Note that the perimeter of a loop is always even!:x
        if (STEPS - it) % 2 == 0:
            cnt += 1

        for dr, dc in DELTAS:
            new_r = r + dr
            new_c = c + dc

            if (new_r, new_c) in SEEN:
                continue

            SEEN.add((new_r, new_c))

            if not (0 <= new_r < ROWS and 0 <= new_c < COLS):
                continue

            if inp[new_r][new_c] == '#':
                continue
            
            if it == STEPS:
                continue

            Q.append((it + 1, new_r, new_c))
    return cnt