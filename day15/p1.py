from typing import List

def hsh(x: str):
    sm = 0
    for ch in x:
        sm += ord(ch)
        sm*= 17
        sm %= 256
    return sm

def solve(inp: List[str]):
    ls = inp[0].split(",")
    return sum([hsh(x) for x in ls])