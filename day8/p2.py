from typing import List
from math import lcm

nodes = {}


def solve(inp: List[str]):
    steps = inp[0]

    curs = []

    for ln in inp[2:]:
        spl = ln.split(" = ")
        node = spl[0]
        spl1 = spl[1][1:-1].split(", ")
        nodes[node] = (spl1[0], spl1[1])

        if node[2] == "A":
            curs.append(node)

    lens = [run_node(node, steps) for node in curs]

    cur = lens[0]

    for c in lens[1:]:
        cur = lcm(cur, c)


    return cur


def run_node(cur, steps):
    i = 0

    while cur[2] != "Z":
        step = steps[i % len(steps)]
        
        dirs = nodes[cur]
        
        cur = dirs[0] if step == "L" else dirs[1]

        i += 1

    return i