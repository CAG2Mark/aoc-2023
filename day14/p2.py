from typing import List
from copy import deepcopy

def rotate(state):
    ret = list(zip(*state[::-1]))
    return [list(x) for x in ret]

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

def print_board(state):
    for ln in state:
        print(''.join(ln))

def extrapolate_cycle(items, length, to):
    c1 = items[-length:]
    c2 = items[-2*length:-length]
    
    if c1 != c2:
        return -1
    
    to -= len(items) % length

    return c1[to % length]

def solve(inp: List[str]):
    state = []
    for ln in inp:
        state.append(list(ln))

    # 1000000000
    l = []
    for i in range(1000):
        if i % 4 == 0:
            # print_board(state)
            l.append(calc_load(state))
        # print_board(state)
        # print()
        move_rocks(state)
        # print_board(state)
        # print(calc_load(state))
        state = rotate(state)
        # print("------------------------------")
    
    for i in range(100):
        cur = extrapolate_cycle(l, i, 1000000000)
        if cur != -1:
            return cur
    
    return -1