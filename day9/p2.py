from typing import List

def is_constant(seq: List[int]):
    first = seq[0]
    for i in seq[1:]:
        if i != first: return False
    return True
    
def extrapolate(seq: List[int]):
    if is_constant(seq):
        seq.append(seq[0])
    else:
        diffs = []
        for i in range(1, len(seq)):
            diffs.append(seq[i] - seq[i - 1])
        extrapolate(diffs)
        seq.insert(0, seq[0] - diffs[0])

sequences = []


def solve(inp: List[str]):
    for ln in inp:
        sequences.append([int(x) for x in ln.split()])
    
    for seq in sequences:
        extrapolate(seq)
    
    return sum([l[0] for l in sequences])