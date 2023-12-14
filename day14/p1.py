from typing import List
from copy import deepcopy

def move_rocks(state):
    for i, row in enumerate(state):
        for j, ch in enumerate(row):
            if ch != 'O': continue

            move_to = i
            # search upwards
            for k in range(i - 1, -2, -1):
                if k == -1 or state[k][j] != '.':
                    move_to = k + 1
                    break
            
            state[i][j] = '.'
            state[move_to][j] = 'O'

def calc_load(state):
    sm = 0
    for i, row in enumerate(state):
        for ch in row:
            if ch != 'O': continue
            sm += len(state) - i
    return sm
    
def solve(inp: List[str]):
    state = []
    for ln in inp:
        state.append(list(ln))

    move_rocks(state)
    
    return calc_load(state)