from typing import List

DIRS = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}
def solve(inp: List[str]):
    filled = set()

    minr = 0
    minc = 0
    maxr = 1
    maxc = 1

    curr = 0
    curc = 0

    filled.add((0, 0))

    for ln in inp:
        spl = ln.split()
        direction = spl[0]
        dist = int(spl[1])

        (dr, dc) = DIRS[direction]

        for _ in range(dist):
            curr += dr
            curc += dc

            filled.add((curr, curc))

            minr = min(minr, curr)
            minc = min(minc, curc)
            maxr = max(maxr, curr + 1)
            maxc = max(maxc, curc + 1)
    
    return interior(filled, minr, minc, maxr, maxc)

def interior(filled, minr, minc, maxr, maxc):
    perimeter = len(filled)

    st = [(minr - 1, minc - 1)]
    while st:
        (r, c) = st.pop()
        for (dr, dc) in DIRS.values():
            newr = r + dr
            newc = c + dc

            if not (minr - 1 <= newr < maxr + 1 and minc - 1 <= newc < maxc + 1):
                continue

            if (newr, newc) in filled:
                continue

            filled.add((newr, newc))
            st.append((newr, newc))

    area = (maxr - minr + 2) * (maxc - minc + 2)
    return area - len(filled) + perimeter
    

        