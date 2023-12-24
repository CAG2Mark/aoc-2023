from typing import List
import z3

def solve(inp: List[str]):
    hailstones = []
    
    for ln in inp:
        spl = ln.split(" @ ")
        pos = [int(x) for x in spl[0].split(", ")]
        vel = [int(x) for x in spl[1].split(", ")]
        hailstones.append((tuple(pos), tuple(vel)))

    hailstones = hailstones
    
    x0 = z3.Real('x0')
    y0 = z3.Real('y0')
    z0 = z3.Real('z0')
    p0 = z3.Real('p0')
    q0 = z3.Real('q0')
    r0 = z3.Real('r0')
    
    s = z3.Solver()
    
    eqns = []
    for i, ((x, y, z), (p, q, r)) in enumerate(hailstones):
        t = z3.Real(f"t{i}")
        eqns.append(x0 + t * p0 == x + t * p)
        eqns.append(y0 + t * q0 == y + t * q)
        eqns.append(z0 + t * r0 == z + t * r)
    
    s.add(*eqns)
    
    s.check()

    return s.model()[x0].as_long() + s.model()[y0].as_long() + s.model()[z0].as_long()