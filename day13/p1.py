from typing import List

def solve_pat(pat):
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
        if check_col(i):
            return i
    
    return 0

def solve_pat_wrap(pat):
    val = solve_pat(pat)

    if val == 0:
        return 100 * solve_pat(transpose(pat))
    return val

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
            ans += solve_pat_wrap(pattern)
            pattern = []
        else:
            pattern.append(ln)
    ans += solve_pat_wrap(pattern)

    return ans