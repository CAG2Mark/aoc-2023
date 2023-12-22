from collections import defaultdict
from typing import List

def lowest_pos(x, y, z, settled):
    diff = 0
    while z - diff > 1 and not (x, y, z - diff - 1) in settled:
        diff += 1

    return diff

def is_airborne(base, settled):
    min_z = 10000000
    for _, _, z in base:
        min_z = min(z, min_z)

    fall = min([lowest_pos(*t, settled) for t in base if t[2] == min_z])
    return fall != 0

def solve(inp: List[str]):
    cubes = []
    for i, ln in enumerate(inp):
        spl = ln.split("~")
        start = [int(x) for x in spl[0].split(",")]
        end = [int(x) for x in spl[1].split(",")]
        cubes.append((i, start, end))
    
    cubes.sort(key=lambda x: min(x[1][2], x[2][2]))
    
    settled = set()

    fallen = []

    at_z = defaultdict(lambda: [])

    for idx, (x1, y1, z1), (x2, y2, z2) in cubes:
        # get base cubes
        base = []
        brick = []

        min_z = 0
        if x1 - x2 != 0:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                base.append((i, y1, z1))
                brick.append((i, y1, z1))
        elif z1 - z2 != 0:
            base.append((x1, y1, min(z1, z2)))
            for i in range(min(z1, z2), max(z1, z2) + 1):
                brick.append((x1, y1, i))
        else:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                base.append((x1, i, z1))
                brick.append((x1, i, z1))
        min_z = min(z1, z2)
    
        
        fall = min([lowest_pos(*t, settled) for t in base])
        #print([lowest_pos(*t, settled) for t in base])
        
        new_brick = []
        for (x, y, z) in brick:
            settled.add((x, y, z - fall))
            new_brick.append((x, y, z - fall))

        fallen.append((idx, new_brick))
        at_z[min_z - fall].append((idx, new_brick))
    
    cnt = 0
    for idx, brick in fallen:
        max_z = max([t[2] for t in brick])

        for t in brick:
            settled.remove(t)
        
        if not any([is_airborne(b, settled) for _, b in at_z[max_z + 1]]):
            # print(idx)
            cnt += 1
        
        for t in brick:
            settled.add(t)
    
    return cnt
