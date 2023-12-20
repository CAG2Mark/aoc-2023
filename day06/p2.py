from typing import List
import math

def near_integer(x: float):
    return abs(x - int(x)) < 1e-12

def solve(inp: List[str]):
    times = [x for x in inp[0].split()[1:]]
    dists = [x for x in inp[1].split()[1:]]

    time = int(''.join(times))
    record = int(''.join(dists))

    ways = 0

    prev = -1

    if False:
        for j in range(time + 1):
            remains = time - j
            speed = j
            dist = remains * speed

            if dist > record:
                ways += 1
            
            if dist < prev:
                break
            
            prev = dist

    # Smart way. (Done after the fact)
    # Solve the quadratic inequality: x * (time - x) - record > 0.
    # <=> x^2 - time * x + record < 0
    # Roots are
    # 1/2(time - sqrt(time^2 - 4*record))
    # 1/2(time + sqrt(time^2 - 4*record))

    lower = 0.5 * (time - math.sqrt(time*time - 4*record))
    upper = 0.5 * (time + math.sqrt(time*time - 4*record))

    d = 0 
    if near_integer(lower):
        d -= 1
    if near_integer(upper):
        d -= 1

        
    return math.floor(upper) - math.ceil(lower) + 1 + d