from typing import List

nmap = {
    '|': [(1, 0), (-1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(0, 1), (1, 0)]
}  

def solve(inp: List[str]):
    sr = -1
    sc = -1
    for (i, ln) in enumerate(inp):
        for (j, ch) in enumerate(ln):
            if ch == 'S':
                sr = i
                sc = j
                break
        if sr != -1:
            break

    deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]

    maxlen = 0
    for (i, j) in deltas:
        newr = sr + i
        newc = sc + j

        if newr < 0 or newc < 0 or newr >= len(inp) or newc >= len(inp[0]):
            continue

        ch = inp[newr][newc]
        if ch == '.': continue

        neighbours = nmap[ch]

        cond = False
        for (dy, dx) in neighbours:
            if (dy, dx) == (-i, -j):
                cond = True
                break
                
        if not cond: continue
        
        maxlen = max(maxlen, find_loop(sr, sc, newr, newc, inp))
    
    return (maxlen + 1) // 2
    
    
def find_loop(r, c, curr, curc, inp):
    l = 1
    visited = set()
    latest = (curr, curc)

    while latest != (r, c):
        i = latest[0]
        j = latest[1]
        
        visited.add((i, j))

        ch = inp[i][j]
        neighbours = nmap[ch]

        found = False
        for (dy, dx) in neighbours:
            newr = i + dy
            newc = j + dx
            if (newr, newc) in visited:
                continue
            if (newr, newc) == (r, c) and (i, j) == (curr, curc):
                continue
                
            latest = (newr, newc)
            l += 1
            found = True
            break
        if not found: return -1

    return l
                 