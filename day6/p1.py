from typing import List

def solve(inp: List[str]):
    times = [int(x) for x in inp[0].split()[1:]]
    dists = [int(x) for x in inp[1].split()[1:]]

    prod = 1
    
    num = len(dists)
    for i in range(num):
        ways = 0
        time = times[i]
        record = dists[i]

        for j in range(time + 1):
            remains = time - j
            speed = j
            dist = remains * speed

            if dist > record:
                ways += 1
        
        prod *= ways
    return prod