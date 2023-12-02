from typing import List

def solve(inp: List[str]):
    sm = 0
    for ln in inp:
        sm += power(ln)
    
    return sm

def toNums(draws):
    red = 0
    green = 0
    blue = 0

    for d in draws:
        num = int(d[0])
        if d[1] == "red":
            red = int(num)
        elif d[1] == "green":
            green = int(num)
        elif d[1] == "blue":
            blue = int(num)
    
    return (red, green, blue)

def power(ln):
    spl = ln.split(": ")[1].split(";")

    maxred = 0
    maxgreen = 0
    maxblue = 0
    
    for draw in spl:
        draws = draw.split(", ")
        draws = [x.strip().split(" ") for x in draws]

        nums = toNums(draws)

        maxred = max(maxred, nums[0])
        maxgreen = max(maxgreen, nums[1])
        maxblue = max(maxblue, nums[2])

    return maxred * maxgreen * maxblue