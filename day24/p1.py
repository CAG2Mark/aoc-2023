from typing import List

def intersect(h1, h2):
    (x1, y1, z1) = h1[0]
    (p1, q1, r1) = h1[1]

    (x2, y2, z2)  = h2[0]
    (p2, q2, r2) = h2[1]

    # x1 + p1 t1 = x2 + p2 t2
    # p2 t2 - p1 t1 = x1 - x2

    # q2 t2 - q1 t1 = y1 - y2

    #
    # [p2  -p1] [t2]     [x1-x2]
    # [q2  -q1] [t1]     [y1-y2]
    # 
    
    det = p1 * q2 - p2 * q1
    if det == 0:
        return None
    
    a = x1 - x2
    b = y1 - y2

    t2 = 1/det * (-q1 * a + p1 * b)
    t1 = 1/det * (-q2 * a + p2 * b)

    if t1 < 0 or t2 < 0:
        return None

    return (x1 + p1 * t1, y1 + q1 * t1)



def solve(inp: List[str]):
    LOWER = 200000000000000
    UPPER = 400000000000000

    hailstones = []
    
    for ln in inp:
        spl = ln.split(" @ ")
        pos = [int(x) for x in spl[0].split(", ")]
        vel = [int(x) for x in spl[1].split(", ")]
        hailstones.append((tuple(pos), tuple(vel)))

    cnt = 0
    for i in range(len(hailstones)):
        for j in range(i + 1, len(hailstones)):
            val = intersect(hailstones[i], hailstones[j])
            if val is None: continue
            (x, y) = val
            if LOWER <= x <= UPPER and LOWER <= y <= UPPER:
                cnt += 1
    return cnt
