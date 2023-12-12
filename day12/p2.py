from typing import List
from functools import cache

@cache
def all_cache(substr):
    return any([x == '.' for x in substr])

def solve_fast(row, items):
    @cache
    def solve_fast_inner(cur_idx, item_idx):
        if cur_idx == len(row):
            if item_idx == len(items):
                return 1
            else:
                return 0
        
        if item_idx == len(items) and row[cur_idx] == '#':
            return 0
        
        def solve_nonempty():
            if item_idx == len(items):
                return 0
            
            item = items[item_idx]

            if len(row) - cur_idx < item:
                return 0
            
            if all_cache(row[cur_idx : cur_idx + item]):
                return 0
            
            if len(row) - cur_idx == item:
                if item_idx == len(items) - 1:
                    return 1
                else:
                    return 0
            
            if row[cur_idx + item] == '#':
                return 0
            
            return solve_fast_inner(cur_idx + item + 1, item_idx + 1)

        def solve_empty():
            return solve_fast_inner(cur_idx + 1, item_idx)

        if row[cur_idx] == '#':  
            return solve_nonempty()
        
        elif row[cur_idx] == '.':
            return solve_empty()
        
        else:
           return solve_nonempty() + solve_empty()
    return solve_fast_inner(0, 0)

@cache
def solve_slow(row, items):
    if not row:
        if items:
            return 0
        else:
            return 1
    
    if not items and row[0] == '#':
        return 0
    
    def solve_nonempty():
        if not items:
            return 0
        item = items[0]

        if len(row) < item:
            return 0
        
        if all_cache(row[:item]):
            return 0

        if len(row) == item:
            if len(items) == 1:
                return 1
            else:
                return 0
        
        if row[item] == '#':
            return 0
        
        return solve_slow(row[item + 1:], tuple(items[1:]))
    
    def solve_empty():
        return solve_slow(row[1:], items)
    
    if row[0] == '#':
        return solve_nonempty()
    elif row[0] == '.':
        return solve_empty()
    else:
        return solve_nonempty() + solve_empty()


def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        spl = ln.split(" ")
        row = (spl[0] + '?') * 5
        row = row[:-1]
        items = tuple([int(x) for x in spl[1].split(",")] * 5)
        
        val = solve_fast(row, items)

        sm += val

    return sm