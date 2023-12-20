from typing import List

conv = []

def run_conv(val, convs):
    for c in convs:
        if val < c[1] or val >= c[1] + c[2]:
            continue
        return val - c[1] + c[0]
    
    return val

def run_convs(val):
    for convs in conv:
        val = run_conv(val, convs)
    return val

def solve(inp: List[str]):
    seeds = inp[0].split(": ")[1].split(" ")
    seeds = [int(x) for x in seeds]
    
    cur = []
    i = 3
    while i < len(inp):
        if inp[i].strip():
            cur.append([int(x) for x in inp[i].split(" ")])
        else:
            conv.append(cur)
            cur = []
            i += 1
        i += 1
    conv.append(cur)
    
    locs = [run_convs(val) for val in seeds]

    return min([run_convs(val) for val in seeds])