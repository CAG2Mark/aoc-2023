from typing import List

nodes = {}

def solve(inp: List[str]):
    steps = inp[0]

    for ln in inp[2:]:
        spl = ln.split(" = ")
        node = spl[0]
        spl1 = spl[1][1:-1].split(", ")
        nodes[node] = (spl1[0], spl1[1])

    cur = "AAA"

    i = 0

    while cur != "ZZZ":
        step = steps[i % len(steps)]
        
        dirs = nodes[cur]
        
        cur = dirs[0] if step == "L" else dirs[1]

        i += 1

    return i