from typing import List

def is_constant(seq: List[int]):
    first = seq[0]
    for i in seq[1:]:
        if i != first: return False
    return True
    
def extrapolate(seq: List[int]):
    if is_constant(seq):
        return seq[0]
    else:
        diffs = []
        for i in range(1, len(seq)):
            diffs.append(seq[i] - seq[i - 1])
        return seq[0] - extrapolate(diffs)

sequences = []

def solve(inp: List[str]):
    for ln in inp:
        sequences.append([int(x) for x in ln.split()])
    
    return sum([extrapolate(l) for l in sequences])