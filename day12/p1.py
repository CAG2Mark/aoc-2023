from typing import List
from collections import deque
from functools import cache

@cache
def solve_row(row, items):
    if not row:
        if items:
            return 0
        else:
            return 1

    if row[0] == '#':  
        if not items:
            return 0
        
        item = items[0]

        if len(row) < item:
            return 0
        
        if any([x == '.' for x in row[:item]]):
            return 0

        if len(row) > item and row[item] == '#':
            return 0
        
        return solve_row(row[item + 1:], tuple(items[1:]))
    
    elif row[0] == '.':
        return solve_row(row[1:], items)
    
    else:
        return solve_row('#' + row[1:], items) + solve_row('.' + row[1:], items)


def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        spl = ln.split(" ")
        row = spl[0]
        items = tuple([int(x) for x in spl[1].split(",")])
        
        val = solve_row(row, items)

        sm += val

    return sm