from typing import List

ROWS = 0
COLS = 0
def expand_num(inp: List[str], row, col):
    global COLS
    start = col
    end = col + 1
    while end < COLS and inp[row][end].isdigit():
        end = end + 1
    while start - 1 >= 0 and inp[row][start - 1].isdigit():
        start = start - 1
    return (start, end)

def solve(inp: List[str]):
    sm = 0

    global ROWS, COLS
    ROWS = len(inp)
    COLS = len(inp[0])

    for (row, ln) in enumerate(inp):
        for (col, ch) in enumerate(ln):
            if not ch.isdigit() and ch != '.':

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        newr = row + i
                        newc = col + j

                        if not (0 <= newr < ROWS and 0 <= newc < COLS):
                            continue

                        if not inp[newr][newc].isdigit(): continue
                            
                        (start, end) = expand_num(inp, newr, newc)

                        sm += int(inp[newr][start:end])

                        inp[newr] = inp[newr][:start] + "." * (end - start) + inp[newr][end:]
    return sm
