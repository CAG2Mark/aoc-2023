from collections import defaultdict
from typing import List

def lowest_pos(x, y, z, settled, max_diff):
    diff = 0
    while diff < max_diff and z - diff > 1 and not (x, y, z - diff - 1) in settled:
        diff += 1

    return diff

def is_airborne(base, settled):
    min_z = 10000000
    for _, _, z in base:
        min_z = min(z, min_z)

    fall = 10000000
    for t in base:
        if t[2] != min_z: continue
        fall = min(fall, lowest_pos(*t, settled, fall))

    return fall != 0

def disintegrate(all_bricks, brick, settled, at_z):
    max_z = max([t[2] for t in brick])

    settled = settled.copy()
    
    for b in brick:
        settled.remove(b)

    affected = set([idx for (idx, _) in at_z[max_z + 1]])

    total = set()

    while affected:
        affected_list = [(i, all_bricks[i]) for i in affected]

        fallen = set([idx for idx, b in affected_list if is_airborne(b, settled)])

        total = total.union(fallen)

        affected = set()

        for idx in fallen:
            brick = all_bricks[idx]
            for b in brick:
                settled.remove(b)

            max_z = max([t[2] for t in brick])
            affected = affected.union([idx for (idx, _) in at_z[max_z + 1] if not idx in total])

    return total

def solve(inp: List[str]):
    cubes = []
    for i, ln in enumerate(inp):
        spl = ln.split("~")
        start = [int(x) for x in spl[0].split(",")]
        end = [int(x) for x in spl[1].split(",")]
        cubes.append((i, start, end))
    
    cubes.sort(key=lambda x: min(x[1][2], x[2][2]))
    
    settled = set()

    fallen = {}

    at_z = defaultdict(lambda: [])

    i = 0
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
    
        
        fall = min([lowest_pos(*t, settled, 100000000) for t in base])
        
        new_brick = []
        for (x, y, z) in brick:
            settled.add((x, y, z - fall))
            new_brick.append((x, y, z - fall))

        fallen[idx] = new_brick
        at_z[min_z - fall].append((idx, new_brick))
    

    total = 0
    i = 0
    for idx, brick in fallen.items():
        i += 1
        val = disintegrate(fallen, brick, settled, at_z)
        total += len(val)
    
    return total
