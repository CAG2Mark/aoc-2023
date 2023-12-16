from typing import List

def solve(inp: List[str]):
    ROWS = len(inp)
    COLS = len(inp[0])
    
    energized = [[0] * COLS for _ in range(ROWS)]

    # r, c dirR, dirC
    beams = [(0, 0, 0, 1)]

    BEEN = set()
    
    while beams:
        b = beams.pop()
        if b in BEEN:
            continue
        BEEN.add(b)

        (r, c, dirR, dirC) = b
        if 0 <= r < ROWS and 0 <= c < COLS:
            ch = inp[r][c]
            energized[r][c] = 1

            if ch == '|' and dirC != 0:
                beams.append((r + 1, c, 1, 0))
                beams.append((r - 1, c, -1, 0))
                continue
            elif ch == '-' and dirR != 0:
                beams.append((r, c - 1, 0, -1))
                beams.append((r, c + 1, 0, 1))
                continue

            if ch == '\\':
                tmp = dirR
                dirR = dirC
                dirC = tmp
            elif ch == '/':
                tmp = -dirR
                dirR = -dirC
                dirC = tmp
            beams.append((r + dirR, c + dirC, dirR, dirC))
            
    return sum([sum(l) for l in energized])