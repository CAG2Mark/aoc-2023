from typing import List

conv = []

def inters(i1, i2):
    lower = max(i1[0], i2[0])
    upper = min(i1[1], i2[1])

    if lower >= upper: return None

    return (lower, upper)

def run_convs(start, end):
    cur = [(start, end)]
    nexts = []
    for convs in conv:
        for c in cur:
            nexts += run_range(c[0], c[1], convs)
        cur = nexts
        nexts = []
    return cur

def run_range(start, end, convs):
    ret = []

    i1 = (start, end)

    i2s = []
    
    # intersection
    for c in convs:
        i2s.append((c[1], c[1] + c[2]))
        
        intc = inters(i1, (c[1], c[1] + c[2]))
        if intc == None: continue

        d = c[0] - c[1]
        ret.append((intc[0] + d, intc[1] + d))

    i2s.sort(key=lambda x: x[0])

    # Compute subtraction of intervals
    # i1 subtract all intervals in conv2
    for i2 in i2s:
        itsc = inters(i1, i2)

        if itsc == None: continue

        new_i = (i1[0], itsc[0])
        if new_i[0] < new_i[1]:
            ret.append(new_i)

        i1 = (itsc[1], i1[1])

        if i1[0] >= i1[1]:
            break
    
    if i1[0] < i1[1]:
        ret.append((i1[0],i1[1]))


    return ret

def solve(inp: List[str]):
    global conv

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

    cur.sort(key=lambda x: x[1])
    conv.append(cur)

    minval = 100000000000000000000

    for i in range(0, len(seeds) - 2, 2):
        ran = run_convs(seeds[i], seeds[i] + seeds[i+1])
        lower = [x[0] for x in ran]

        minval = min(min(lower), minval)
    return minval
