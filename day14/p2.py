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


def state_tostr(state):
    return ''.join([''.join(r) for r in state])

def solve(inp: List[str]):
    state = []
    for ln in inp:
        state.append(list(ln))

    # 1000000000
    SEEN = {}
    
    i = 0
    skipped = False
    N = 1000000000
    while i < N:
        if not skipped:
            s = state_tostr(state)
            if s in SEEN:
                skipped = True
                d = i - SEEN[s]
                i += ((N - i) // d) * d
            else:
                SEEN[s] = i


        for _ in range(4):
            move_rocks(state)
            state = rotate(state)
    
        i += 1
    
    return calc_load(state)

def solve_old(inp: List[str]):
    state = []
    for ln in inp:
        state.append(list(ln))

    # 1000000000
    l = []
    for i in range(1000000000 * 4):
        if i % 4 == 0:
            # print_board(state)
            l.append(calc_load(state))

            for j in range(i // 2):
                cur = extrapolate_cycle(l, j, 1000000000)
                if cur != -1:
                    return cur
        # print_board(state)
        # print()
        move_rocks(state)
        # print_board(state)
        # print(calc_load(state))
        state = rotate(state)
        # print("------------------------------")
    
    return calc_load(state)