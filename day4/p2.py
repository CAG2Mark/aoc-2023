from typing import List

def solve(inp: List[str]):
    l = [1] * len(inp)
    for (i, ln) in enumerate(inp):
        spl = ln.split(": ")[1].split(" | ")
        spl = [x.strip() for x in spl]

        win = [int(x) for x in spl[0].split(" ") if x]
        card = [int(x) for x in spl[1].split(" ") if x]

        num = len(set(win).intersection(set(card)))

        for j in range(i + 1, i + num + 1):
            l[j] += l[i]
    
    return sum(l)
