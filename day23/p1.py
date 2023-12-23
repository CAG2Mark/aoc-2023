from typing import List

def neighbours(inp, row, col):
    DELTAS = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    ROWS = len(inp)
    COLS = len(inp[0])
    
    ch = inp[row][col]
    if ch == '>': return [(row, col + 1)]
    if ch == '<': return [(row, col - 1)]
    if ch == '^': return [(row - 1, col)]
    if ch == 'v': return [(row + 1, col)]

    ret = []
    for dr, dc in DELTAS:
        newr = row + dr
        newc = col + dc

        if not (0 <= newr < ROWS and 0 <= newc < COLS):
            continue
        
        ch = inp[newr][newc]

        if ch == '#':
            continue

        if ch == '>' and dc == -1:
            continue
        if ch == '<' and dc == 1:
            continue
        if ch == '^' and dr == 1:
            continue
        if ch == 'v' and dr == -1:
            continue
  
        ret.append((newr, newc))
    return ret

def search_poi(inp, row, col, end):
    st = [(row, col)]

    VISITED = set()
    VISITED.add((row, col))
    
    ret = []

    while st:
        cur = st.pop()
        n = neighbours(inp, *cur)

        for r, c in n:
            if (r, c) in VISITED:
                continue
            
            ch = inp[r][c]

            if (r, c) == end:
                ret.append((r, c))

            if ch in ['>', '^', '<', 'v']:
                ret.append((r, c))
                continue

            VISITED.add((r, c))
            st.append((r, c))
    
    return ret

def longest_path(inp, source, dest, visited, ignore):
    if source == dest:
        return 0
    
    ne = neighbours(inp, *source)
    visited.add(source)
    
    maxlen = float('-inf')

    for n in ne:
        if n in visited:
            continue

        if n != dest and n in ignore:
            continue
    
        #print(n)
        lp = longest_path(inp, n, dest, visited, ignore)
        maxlen = max(maxlen, lp)

    visited.remove(source)

    return maxlen + 1

# solve using dp, it's a directed acyclic graph
cache = {}
def longest_path_overall(lps, source, end):
    if source == end:
        return 0
    
    if source in cache:
        return cache[source]

    assert source in lps
    
    maxlen = 0
    for after, cost in lps[source]:
        #print(after)
        ans = cost + longest_path_overall(lps, after, end)
        maxlen = max(maxlen, ans)
    
    cache[source] = maxlen
    
    return maxlen

def solve(inp: List[str]):
    ROWS = len(inp)
    COLS = len(inp[0])
    
    start = (0, 1)
    end = (ROWS - 1, COLS - 2)

    # Too slow to search directly.
    # Idea: From each slope, and ths start find all other slopes you can reach
    # call these

    poi = [start]
    for i, ln in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch in ['>', '^', '<', 'v']:
                poi.append((i, j))
    
    reachable = []
    for r, c in poi:
        reachable.append(((r, c), search_poi(inp, r, c, end)))

    lps = {}
    # between each poi, find the longest path
    for (r, c), pois in reachable:
        poi_lp = []

        for rr, cc in pois:
            lp = longest_path(inp, (r, c), (rr, cc), set(), set(pois))
            poi_lp.append(((rr, cc), lp))
        
        lps[(r, c)] = poi_lp
    
    return longest_path_overall(lps, start, end)
    

