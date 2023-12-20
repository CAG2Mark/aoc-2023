from typing import List
from collections import deque
from collections import defaultdict

edges = {}
flipflops = defaultdict(lambda: False)
conjs = {}

def run_once(targets):
    pulses = deque()
    # False = Low, True = High
    pulses.append(("broadcaster", False, "button"))

    newpulses = deque()

    i = -1
    ret = {t: -1 for t in targets}

    while pulses:
        # print(pulses)
        for dest, pulse, source in pulses:
        #print(source + " --> " + dest + " " + str(pulse))   
            if not dest in edges:
                continue
            (ty, name, dests) = edges[dest]

            if dest in targets and not pulse:
                ret[dest] = i

            if ty == 'B':
                for n in dests:
                    newpulses.append((n, False, name))
            elif ty == '%':
                if pulse: continue

                flipflops[name] = not flipflops[name]
                out = flipflops[name]

                for n in dests:
                    newpulses.append((n, out, name))
            else: # ty == '&'
                conjs[name][source] = pulse
                out = not all(conjs[name].values())

                for n in dests:
                    newpulses.append((n, out, name))

        pulses = newpulses
        newpulses = deque()
        i += 1
        # print(i, )
        # print(conjs["lb"])
        

    return ret

def solve(inp: List[str]):
    final = None

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

            if "rx" in dests:
                final = name


    for (_, name, dests) in edges.values():
        for d in dests:
            if not d in edges: continue

            (ty, _, _) = edges[d]
            if ty != '&': continue

            conjs[d][name] = False

    targets = { key: [] for key in conjs[final].keys() }

    def satisfied():
        for l in targets.values():
            if not (len(l) > 2 and l[-1] - l[-2] == l[-2] - l[-3]):
                return False
        return True
    
    i = 1
    on = -1
    while not satisfied():
        result = run_once(targets.keys())
        
        for k, val in result.items():
            if val != -1: 
                targets[k].append(i)
                assert(on == -1 or val == on)
                on = val
        i += 1
    
    prod = 1
    for l in targets.values():
        prod *= l[-1] - l[-2]

    return prod