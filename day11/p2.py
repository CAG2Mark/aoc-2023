from typing import List

galaxies = []
def solve(inp: List[str]):
    ROWS = len(inp)
    COLS = len(inp[0])
    
    for (i, ln) in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch == '#':
                galaxies.append((i, j))
    
    empty_r = [True] * ROWS
    empty_c = [True] * COLS

    for i in range(ROWS):
        for r, _ in galaxies:
            if r == i:
                empty_r[i] = False
                break
    
    for i in range(COLS):
        for _, c in galaxies:
            if c == i:
                empty_c[i] = False
                break

    r_dist = [[0] * ROWS for _ in range(ROWS)]
    c_dist = [[0] * COLS for _ in range(COLS)]

    for i in range(ROWS):
        for j in range(i + 1, ROWS):
            r_dist[i][j] = r_dist[i][j - 1] + 1 + empty_r[j - 1] * (1000000 - 1)
            r_dist[j][i] = r_dist[i][j]
    
    for i in range(COLS):
        for j in range(i + 1, COLS):
            c_dist[i][j] = c_dist[i][j - 1] + 1 + empty_c[j - 1] * (1000000 - 1)
            c_dist[j][i] = c_dist[i][j]

    sm = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            (r1, c1) = galaxies[i]
            (r2, c2) = galaxies[j]
            sm += r_dist[r1][r2] + c_dist[c1][c2]
    return sm