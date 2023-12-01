from typing import List

digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        cur = ''
        for i in range(len(ln)):
            chr = ln[i]
            if chr.isdigit():
                cur += chr
            else:
                for (j, d) in enumerate(digits):
                    if ln.startswith(d, i):
                        cur += str(j + 1)
        if cur:
            x = cur[0] + cur[-1]
            sm += int(x)
    return sm
