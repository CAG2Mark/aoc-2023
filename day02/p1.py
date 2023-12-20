from typing import List

RED = 12
GREEN = 13
BLUE = 14

def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        gameid = int(ln.split(" ")[1][:-1])

        if not isDrawsGood(ln): continue
        sm += gameid
    
    return sm

def isGood(draws):
    for d in draws:
        num = int(d[0])
        if d[1] == "red" and int(num) > RED:
            return False
        elif d[1] == "green" and int(num) > GREEN:
            return False
        elif d[1] == "blue" and int(num) > BLUE:
            return False
    return True

def isDrawsGood(ln):
    spl = ln.split(": ")[1].split(";")
    for draw in spl:
        draws = draw.split(", ")
        draws = [x.strip().split(" ") for x in draws]

        if not isGood(draws):
            return False
    return True