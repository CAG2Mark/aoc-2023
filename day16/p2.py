from typing import List

def solve_for(start, inp):
    ROWS = len(inp)
    COLS = len(inp[0])

    energized = [[0] * COLS for _ in range(ROWS)]

    # r, c dirR, dirC
    beams = [start]
    newbeams = []


    BEEN = set()
    
    while beams:
        for b in beams:
            if b in BEEN:
                continue
            BEEN.add(b)

            (r, c, dirR, dirC) = b
            if 0 <= r < ROWS and 0 <= c < COLS:
                ch = inp[r][c]
                energized[r][c] = 1

                if ch == '|' and dirC != 0:
                    newbeams.append((r + 1, c, 1, 0))
                    newbeams.append((r - 1, c, -1, 0))
                    continue
                elif ch == '-' and dirR != 0:
                    newbeams.append((r, c - 1, 0, -1))
                    newbeams.append((r, c + 1, 0, 1))
                    continue

                if ch == '\\':
                    tmp = dirR
                    dirR = dirC
                    dirC = tmp
                elif ch == '/':
                    tmp = -dirR
                    dirR = -dirC
                    dirC = tmp
                newbeams.append((r + dirR, c + dirC, dirR, dirC))
            
        beams = newbeams
        newbeams = []

    return sum([sum(l) for l in energized])

def solve(inp: List[str]):
    ROWS = len(inp)
    COLS = len(inp[0])

    m = 0
    for i in range(ROWS):
        m = max(m, solve_for((i, 0, 0, 1), inp))
        m = max(m, solve_for((i, COLS - 1, 0, -1), inp))
    for i in range(COLS):
        m = max(m, solve_for((0, i, 1, 0), inp))
        m = max(m, solve_for((ROWS - 1, i, -1, 0), inp))
    
    return m
