from typing import List

# always go COUNTER CLOCKWISE
nmap = {
    '|': [(-1, 0), (1, 0)],
    '-': [(0, 1), (0, -1)],
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(0, -1), (1, 0)],
    'F': [(1, 0), (0, 1)]
}  

deltas = [(-1, 0), (0, -1), (0, 1), (1, 0)]

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

    maxlen = 0
    maxloop = []
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
        
        loop = find_loop(sr, sc, newr, newc, inp)
        if len(loop) >= maxlen:
            maxlen = len(loop)
            maxloop = loop
        
    return find_tiles(maxloop, inp)
    
def find_loop(r, c, curr, curc, inp):
    l = [(r, c)]
    visited = set()
    latest = (curr, curc)

    while latest != (r, c):
        i = latest[0]
        j = latest[1]

        l.append((i, j))
        
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
            found = True
            break
        if not found: return -1

    return l

def find_tiles(loop, inp):
    filled = set(loop)
    run_loop(inp, filled, loop)

    if (-1, 0) in filled: # test position to check if it is outside
        l = len(filled) - 1
        # take the complement
        return len(inp) * len(inp[0]) - l

    return len(filled) - len(loop)


def run_loop(inp, filled, loop):
    # if loop goes clockwise, this fills the outside
    # otherwise, it fills the inside
    for idx, (i, j) in enumerate(loop):
        (pi, pj) = loop[idx - 1]

        (dy, dx) = (i - pi, j - pj)

        ch = inp[i][j]

        if dy == 1: # going down
            # always on right
            fill_tile(inp, filled, i, j + 1)
            # additionally, if turning left, check the tile below
            if ch == 'J':
                fill_tile(inp, filled, i + 1, j)
        elif dy == -1: # going up
            # alawys left
            fill_tile(inp, filled, i, j - 1)
            # additionally, if turning right, check the the tile above
            if ch == 'F':
                fill_tile(inp, filled, i - 1, j)
        elif dx == 1: # going right
            # always above
            fill_tile(inp, filled, i - 1, j)
        else: # going left
            # always below
            fill_tile(inp, filled, i + 1, j)
            
def fill_tile(inp, filled, i, j):
    if (i, j) in filled:
        return
    
    if (i < 0 or j < 0 or i >= len(inp) or j >= len(inp[0])):
        return

    st = []
    st.append((i, j))    
    filled.add((i, j))

    while st:
        (r, c) = st.pop()

        for (i, j) in deltas:
            newr = r + i
            newc = c + j
            
            if (newr, newc) != (-1, 0) and (newr < 0 or newc < 0 or newr >= len(inp) or newc >= len(inp[0])):
                continue
            
            if (newr, newc) in filled:
                continue
            
            filled.add((newr, newc))
            st.append((newr, newc))