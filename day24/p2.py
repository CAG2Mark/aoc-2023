from typing import List
from collections import defaultdict

# Copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python.
from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def factors(n):
    f = set()
    
    while n % 2 == 0:
        f.add(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            n //= i
            f.add(i)
            continue
        i += 2
    
    if n != 1:
        f.add(n)
    return f

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def solve_z3(hailstones):
    import z3
    
    x0 = z3.Real('x0')
    y0 = z3.Real('y0')
    z0 = z3.Real('z0')
    p0 = z3.Real('p0')
    q0 = z3.Real('q0')
    r0 = z3.Real('r0')
    
    s = z3.Solver()

    hailstones = hailstones[:3]
    
    eqns = []
    for i, ((x, y, z), (p, q, r)) in enumerate(hailstones):
        t = z3.Real(f"t{i}")
        eqns.append(x0 + t * p0 == x + t * p)
        eqns.append(y0 + t * q0 == y + t * q)
        eqns.append(z0 + t * r0 == z + t * r)
    
    s.add(*eqns)
    
    s.check()
    print(s.model())
    return s.model()[x0].as_long() + s.model()[y0].as_long() + s.model()[z0].as_long()

def solve_axis(pos, vel):
    import math
    # This solution assumes that the stone and the hailstones all intersect at *integer timestamps*.
    # It does NOT work on the example input because the Chinese Remainder Theorem only returns an answer
    # up to modulo p1 * p2 * ... * pn, which are small for the example input.
    #
    # We solve on each dimension. Without loss of generality, we solve on the x dimension first.
    # Denote the positions xi and velocities vi, starting position x0, starting velocity v0,
    # and time of intersection for each hailstone i as ti.
    #
    # For any pair i, j, we must have:
    #   position stone i - position stone j = original velocity * time diff
    # i.e.
    #   xi + ti * vi - xj - tj * vj = v0 (ti - tj).
    # 
    # In case vi = vj, of which there are several examples of, we have:
    #
    #   xi - xj + (ti - tj)(v0 - vi) = 0
    # implying
    #   xi - xj = 0 (mod v0 - vi).

    # First we find examples of vi = vj.
    c = defaultdict(lambda: [])
    for (p, vi) in zip(pos, vel):
        c[vi].append(p)
    c = list(c.items())
    c.sort(key=lambda x: -len(x[1]))
    
    # Take the first one
    (vi, plist) = c[0]
    
    cur = -1
    for i in range(len(plist)):
        for j in range(i + 1, len(plist)):
            # Here we try to find the value of v0 - vi.
            # We use the fact that
            #   xi - xj = 0 (mod v0 - vi)
            # and also that
            #   a = 0 (mod n), b = 0 (mod n) 
            # implies a = pn, b = qn, 
            # thus gcd(a, b) is a multiple of n. In fact, gcd(a, b) = gcd(p, q) * n.
            xi = plist[i]
            xj = plist[j]
            if cur == -1:
                cur = abs(xi - xj)
            else:
                cur = math.gcd(xi - xj, cur)

    # This gives an upper bound for |v0 - vi|. Namely, |v0 - vi| < cur.
    
    def tryVel(v0):
        # Now we solve for the original position using the Chinese Remainder Theorem.
        # Note that the original position x0 must satisfy
        #   x0 + ti * v0 = xi + ti * vi
        # i.e.
        #   x0 - xi + ti * (v0 - vi) = 0
        # implying
        #   x0 = xi (mod v0 - vi).
        # Because xi, v0 and vi are known, we can solve for x0 using the Chinese Remainder Theorem.
        divisors = [v0 - vi for vi in vel]
        primed = {}
        for p, v in zip(pos, divisors):
            if v == 0: continue
            if v < 0: v = -v
            if v == 1: continue

            fs = factors(v)
            for f in fs:
                if f in primed and primed[f] != p % f:
                    return None
                
                primed[f] = (p % f)

        # print(primed)

        a = [x[0] for x in primed.items()]
        n = [x[1] for x in primed.items()]

        return chinese_remainder(a, n)

    # Note that from before, we found the bound |v0 - vi| < cur. Also note that
    #   |v0 - vi| < cur <=> -cur < v0 - vi < cur.
    # p is our v0 - vi, add vi to get back v0.
    # This range is small, so we just try all possibilities.
    for p in range(-cur, cur + 1):
        ans = tryVel(p + vi)
        if ans is not None:
            return ans

def solve_crt(hailstones):
    sm = 0
    for i in range(3):
        pos = [x[0][i] for x in hailstones]
        vel = [x[1][i] for x in hailstones]
        sm += solve_axis(pos, vel)
    return sm
        

def solve(inp: List[str]):
    hailstones = []
    
    for ln in inp:
        spl = ln.split(" @ ")
        pos = [int(x) for x in spl[0].split(", ")]
        vel = [int(x) for x in spl[1].split(", ")]
        hailstones.append((tuple(pos), tuple(vel)))

    return solve_crt(hailstones)