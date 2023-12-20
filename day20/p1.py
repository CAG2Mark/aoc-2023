from typing import List
from collections import deque
from collections import defaultdict

edges = {}
flipflops = defaultdict(lambda: False)
conjs = {}

def run_once():
    pulses = deque()
    # False = Low, True = High
    pulses.append(("broadcaster", False, "button"))

    low = 0
    high = 0

    while pulses:
        # print(pulses)
        (dest, pulse, source) = pulses.popleft()
        #print(source + " --> " + dest + " " + str(pulse))

        if pulse:
            high += 1
        else:
            low += 1

        if not dest in edges:
            continue
        (ty, name, dests) = edges[dest]

        if ty == 'B':
            for n in dests:
                pulses.append((n, False, name))
        elif ty == '%':
            if pulse: continue

            flipflops[name] = not flipflops[name]
            out = flipflops[name]

            for n in dests:
                pulses.append((n, out, name))
        else: # ty == '&'
            conjs[name][source] = pulse
            out = not all(conjs[name].values())

            for n in dests:
                pulses.append((n, out, name))

    return (low, high)

def solve(inp: List[str]):
    for ln in inp:
        spl = ln.split(" -> ")
        source = spl[0]
        dests = spl[1].split(", ")
        if source == "broadcaster":
            edge = ("B", source, dests)
            edges["broadcaster"] = edge
        else:
            edge = (source[0], source[1:], dests)
            edges[source[1:]] = edge

            (ty, name, dests) = edge

            if ty == '&':
                conjs[name] = {}
    
    for (_, name, dests) in edges.values():
        for d in dests:
            if not d in edges: continue

            (ty, _, _) = edges[d]
            if ty != '&': continue

            conjs[d][name] = False

    #print(conjs)
    
    ls = 0
    hs = 0
    for i in range(1000):
        (l, h) = run_once()
        ls += l
        hs += h
        #print()

    print(ls, hs)
    return ls*hs