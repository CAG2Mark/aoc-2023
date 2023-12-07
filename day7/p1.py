from typing import List

from functools import cmp_to_key

from collections import defaultdict

def handtype(card):
    d = defaultdict(lambda: 0)
    for ch in card:
        d[ch] += 1
    
    has3 = False
    has2 = False

    twos = set()
    for (k, v) in d.items():
        if v == 5: return 8
        if v == 4: return 7

        if v == 3: has3 = True
        if v == 2: 
            has2 = True
            twos.add(k)
    
    if has3 and has2:
        return 6 # Full house
    
    if has3:
        return 5 # Three of a kind
    
    if len(twos) >= 2:
        return 4 # Two pair
    
    if len(twos) == 1:
        return 3 # One pair
    
    return 2 # High card

cardvals = "AKQJT98765432"

cardmap = {}

def compare(card1, card2):
    c1 = card1[0]
    c2 = card2[0]

    t1 = handtype(c1)
    t2 = handtype(c2)

    if t1 < t2: return -1
    elif t1 > t2: return 1

    for i in range(5):
        p1 = cardmap[c1[i]]
        p2 = cardmap[c2[i]]

        if p1 < p2: return -1
        elif p1 > p2: return 1
        
    return 0

# temporary method I used when the comparator didn't work for some reason...
def tokey(card):
    c = card[0]
    t = handtype(c)

    t *= 1000000000000
    for i in range(5):
        t += 100**(4 - i) * cardmap[c[i]]

    return t

def solve(inp: List[str]):
    for i in range(len(cardvals)):
        cardmap[cardvals[i]] = len(cardvals) - i - 1

    cards = [(ln.split()[0], int(ln.split()[1])) for ln in inp]

    k = cmp_to_key(compare)
        
    cardssorted = sorted(cards, key=k)

    sm = 0
    for (i, v) in enumerate(cardssorted):
        sm += (i + 1) * v[1]

    return sm