from typing import List
from collections import deque

DELTAS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def count_num(inp: List[str], start, start_it, steps):
    ROWS = len(inp)
    COLS = len(inp[0])

    Q = deque()
    Q.append((start_it, *start))
    SEEN = set()
    SEEN.add(start) 
    cnt = 0

    while Q:
        (it, r, c) = Q.popleft()

        # Note that the perimeter of a loop is always even!
        if (steps - it) % 2 == 0:
            cnt += 1
        
        if it == steps:
            continue

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

            Q.append((it + 1, new_r, new_c))

    return cnt

def solve(inp: List[str]):
    ROWS = len(inp)

    NUM = 26501365
    #NUM = 5
    #NUM = 50

    r = -1
    c = -1

    rocks = 0
    empty = 0
    for i, ln in enumerate(inp):
        for j, ch in enumerate(ln):
            if ch == 'S':
                r = i
                c = j
            if ch == '#':
                rocks += 1
            else:
                empty += 1
    
    # Makes use of some assumptions...
    # In my input:
    # num rows = num cols.
    # num rows is odd. (makes it trickier, it's easier if it's even)
    # The paths are nice in that you can go straight down the middle or diagonally along the grid.
    # 
    # This means we can calculate exactly which grids will be filled.
    # 
    # Also, the shortest path towards any tile is the Manhattan distance between the starting point
    # and the nearest edge on its perimeter.

    radius = ((NUM - r + ROWS) + ROWS - 1) // ROWS
    needed_steps = r + 1 + (radius - 2) * ROWS

    # calculate number of cells reachable in odd and even tiles
    # starting tile is marked as odd
    odd = count_num(inp, (r, c), 10000000000, NUM)

    even = count_num(inp, (r, c + 1), 10000000000, NUM)

    total = 0
    # note that the following are equivalent:
    # a cell is reachable in even number of steps 
    # <=> it is not reachable in odd number of steps
    # <=> it is reachable in exactly an even number of steps

    # Don't calculate stuff on the perimeter
    for i in range(1, radius - 1):
        # Number of tiles in diamond of radius i is:
        # Total width = 2 * i - 1
        # width * 2 - 2 
        # -> tiles = (2 * i - 1) * 2 - 2
        #          = 4 * i - 4
        # if i > 1, 1 otherwise

        tiles = 1 if i == 1 else 4 * i - 4
        # start off with odd tiles
        num = odd if i % 2 else even

        total += tiles * num
        # total += tiles * num
    
    # Now calculate the edge tiles.
    
    #          1T2
    #         1AtB2
    #        1Aa.bB2
    #       1Aa...bB2
    #       Ll.....rR
    #       4Dd...cC3
    #        4Dd.cC3
    #         4DbC3
    #          4B3


    # L
    total += count_num(inp, (r, ROWS - 1), needed_steps, NUM)
    # l
    total += count_num(inp, (r, ROWS - 1), needed_steps - ROWS, NUM)
    # R
    total += count_num(inp, (r, 0), needed_steps, NUM)
    # r
    total += count_num(inp, (r, 0), needed_steps - ROWS, NUM)
    # T
    total += count_num(inp, (ROWS - 1, c), needed_steps, NUM)
    # t
    total += count_num(inp, (ROWS - 1, c), needed_steps - ROWS, NUM)
    # B
    total += count_num(inp, (0, c), needed_steps, NUM)
    # b
    total += count_num(inp, (0, c), needed_steps - ROWS, NUM)
    
    edges_mid = max(radius - 2, 0)
    edges_inner = max(radius - 3, 0)

    edges_outer = max(radius - 1, 0)
    
    diag_needed = needed_steps + (ROWS + 1) // 2

    # A
    total += edges_outer * count_num(inp, (ROWS - 1, ROWS - 1), diag_needed, NUM)
    # B
    total += edges_outer * count_num(inp, (ROWS - 1, 0), diag_needed, NUM)
    # C
    total += edges_outer * count_num(inp, (0, 0), diag_needed, NUM)
    # D
    total += edges_outer * count_num(inp, (0, ROWS - 1), diag_needed, NUM)

    # A
    total += edges_mid * count_num(inp, (ROWS - 1, ROWS - 1), diag_needed - ROWS, NUM)
    # a
    total += edges_inner * count_num(inp, (ROWS - 1, ROWS - 1), diag_needed - 2 * ROWS, NUM)
    # B
    total += edges_mid * count_num(inp, (ROWS - 1, 0), diag_needed - ROWS, NUM)
    # b
    total += edges_inner * count_num(inp, (ROWS - 1, 0), diag_needed - 2 * ROWS, NUM)
    # C
    total += edges_mid * count_num(inp, (0, 0), diag_needed - ROWS, NUM)
    # c
    total += edges_inner * count_num(inp, (0, 0), diag_needed - 2 * ROWS, NUM)
    # D
    total += edges_mid * count_num(inp, (0, ROWS - 1), diag_needed - ROWS, NUM)
    # d
    total += edges_inner * count_num(inp, (0, ROWS - 1), diag_needed - 2 * ROWS, NUM)

    return total