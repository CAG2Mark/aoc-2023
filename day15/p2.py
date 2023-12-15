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
    boxes = [[] for _ in range(256)]

    for instr in ls:
        if '=' in instr:
            label = instr.split("=")[0]
            num = int(instr.split("=")[1])
            boxid = hsh(label)

            tmp = []
            added = False
            box = boxes[boxid]
            for i in range(len(box)):
                (l, _) = box[i]
                if label == l:
                    box[i] = (l, num)
                    added = True

            if not added:
                boxes[boxid].append((label, num))
        else:
            label = instr[:-1]
            boxid = hsh(label)

            boxes[boxid] = [x for x in boxes[boxid] if x[0] != label]

    ans = 0
    for i, b in enumerate(boxes):
        for j, (_, val) in enumerate(b):
            ans += (i+1)*(j+1)*val
    return ans