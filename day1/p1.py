from typing import List

def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        cur = ''
        for chr in ln:
            if ord(chr) < ord('0') or ord(chr) > ord('9'): continue
            cur += chr
        if cur:
            x = cur[0] + cur[-1]
            sm += int(x)
    return sm
