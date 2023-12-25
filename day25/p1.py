from typing import List
from collections import defaultdict
from collections import deque

groups = defaultdict(lambda: set())

def search(first):
    VISITED = set()
    VISITED.add(first)
    st = [first]
    g = 0
    while st:
        item = st.pop()
        g += 1
        for n in groups[item]:
            if n in VISITED: continue
            st.append(n)
            VISITED.add(n)
    return g

def findpaths(src):
    VISITED = set()
    VISITED.add(src)
    Q = deque()
    Q.append(src)

    prev = {}

    while Q:
        item = Q.popleft()

        for n in groups[item]:
            if n in VISITED: continue
            Q.append(n)
            VISITED.add(n)
            prev[n] = item

    return prev

def get_most_used(nodes):
    cntr = defaultdict(lambda: 0)

    for i in range(len(nodes)):
        prev = findpaths(nodes[i])

        for j in range(i + 1, len(nodes)):
            cur = nodes[j]
            while cur != nodes[i]:
                temp = cur
                cur = prev[cur]
                n1 = temp
                n2 = cur
                if n1 < n2:
                    cntr[(n1, n2)] += 1
                else:
                    cntr[(n2, n1)] += 1
    l = list(cntr.items())
    l.sort(key=lambda x: x[1])
    return l[-1][0]

def solve(inp: List[str]):
    nodes = set()
    for ln in inp:
        s = ln.split(": ")
        src = s[0]
        others = set(s[1].split())
        groups[src] = groups[src].union(others)

        nodes.add(src)

        for o in others:
            groups[o].add(src)
            nodes.add(o)
    
    nodes = list(nodes)

    for i in range(3):
        src, dest = get_most_used(nodes)
        print(src, dest)
        groups[src].remove(dest)
        groups[dest].remove(src)
    
    g = search(nodes[0])
    print(g)
    print(len(nodes))
    return g * (len(nodes) - g)