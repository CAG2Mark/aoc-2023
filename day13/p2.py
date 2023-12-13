from typing import List
from copy import deepcopy

def solve_pat(pat, ignore):
    ROWS = len(pat)
    COLS = len(pat[0])

    def check_col(col):

        dist = min(col, COLS - col)

        for j in range(dist):
            left = i - j - 1
            right = i + j

            for k in range(ROWS):
                if pat[k][left] != pat[k][right]:
                    return False
        
        return True
    
    for i in range(1, COLS):
        if i == ignore: continue

        if check_col(i):
            return i
    
    return 0

def solve_pat_wrap(pat, ignore = None):
    col_ignore = -1
    row_ignore = -1
    if ignore:
        if ignore[1]: row_ignore = ignore[0]
        else: col_ignore = ignore[0]

    val = solve_pat(pat, col_ignore)

    if val == 0:
        return (solve_pat(transpose(pat), row_ignore), True)
    return (val, False)

def try_different(pat):
    patc = deepcopy(pat)
    patc = [list(x) for x in patc]

    og = solve_pat_wrap(patc)

    for i, row in enumerate(patc):
        for j, col in enumerate(row):
            if col == '#':
                row[j] = '.'
            else:
                row[j] = '#'

            val = solve_pat_wrap(patc, og)
            
            if val == og or val[0] == 0:
                if col == '#':
                    row[j] = '#'
                else:
                    row[j] = '.'
                continue   
            
            if val[1]:
                return 100 * val[0]
            return val[0]

def transpose(pat):
    ROWS = len(pat)
    COLS = len(pat[0])

    ret = [[" "] * ROWS for _ in range(COLS)]

    for i in range(ROWS):
        for j in range(COLS):
            ret[j][i] = pat[i][j]

    return ret
        

def solve(inp: List[str]):
    pattern = []
    ans = 0
    for ln in inp:
        if not ln:
            ans += try_different(pattern)
            pattern = []
        else:
            pattern.append(ln)
    ans += try_different(pattern)

    return ans