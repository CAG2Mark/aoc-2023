from typing import List

def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        spl = ln.split(": ")[1].split(" | ")
        spl = [x.strip() for x in spl]

        win = [int(x) for x in spl[0].split(" ") if x]
        card = [int(x) for x in spl[1].split(" ") if x]

        num = len(set(win).intersection(set(card)))

        if num == 0: continue
        sm += 2 ** (num - 1)

    return sm