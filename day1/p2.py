from typing import List

digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        cur = ''
        for i in range(len(ln)):
            chr = ln[i]
            if ord(chr) < ord('0') or ord(chr) > ord('9'):
                for (j, d) in enumerate(digits):
                    if ln[i:].startswith(d):
                        cur += str(j)
            else:
                cur += chr
        if cur:
            x = cur[0] + cur[-1]
            sm += int(x)
    return sm
