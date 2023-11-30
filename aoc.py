#!/usr/bin/python3

import argparse
import os
import requests

YEAR = 2022

parser = argparse.ArgumentParser(
                    prog='aoc-run')

parser.add_argument('day')
parser.add_argument('-f', '--force-input', action='store_true') # Force fetch input
parser.add_argument('-n', '--no-run', action='store_true') # Do not run
parser.add_argument('-p', '--part') # Part. If none provided then both are run
parser.add_argument('-e', '--use-example', action='store_true') # Use "ex" file instead

args = parser.parse_args()

day = args.day
force_input = args.force_input
part = args.part
norun = args.no_run
use_example = args.use_example

session = open("session", "r").read()
cookies = {"session": session}

daypath = f"day{day}"

if not os.path.exists(daypath):
    os.mkdir(f"{daypath}")

    template = open("TEMPLATE.py", "r").read()
    
    with open(f"{daypath}/p1.py", "w") as f:
        f.write(template)
    
    with open(f"{daypath}/p2.py", "w") as f:
        f.write(template)

input_exists = os.path.exists(f"{daypath}/input")

if force_input or not input_exists:
    print("Downloading input...")
    data = requests.get(f"https://adventofcode.com/{YEAR}/day/{day}/input", cookies=cookies)
    if (data.status_code != 200):
        print(f"Could not download input (error code: {data.status_code}).")
    else:
        print("First 5 lines:")

        data = data.text
        
        spl = data.splitlines()
        for i in range(min(len(spl), 5)):
            print(spl[i])
        
        with open(f"{daypath}/input", "w") as f:
            f.write(data)

def run_all():
    if norun: return

    if use_example:
        if not os.path.exists(f"{daypath}/ex"):
            print("[ERORR] Example file does not exist.")
            return
        else:
            print("NOTE: Using example input!")

    inpfile = "ex" if use_example else "input"

    with open(f"{daypath}/{inpfile}", "r") as f:
        inp = f.read()

    if part == None or part == "1":
        run(1, inp)
    
    if part == None or part == "2":
        run(2, inp)

def run(part: int, inp: str):
    print("-------------------")
    if not os.path.exists(f"{daypath}/p{part}.py"):
        print(f"Could not run part {part} because the file does not exist.")
        print("-------------------")
        return
    
    print(f"PART {part}:")
    p = getattr(__import__(daypath, fromlist=[f"p{part}"]), f"p{part}")
    answer = p.solve(inp.splitlines())

    print("--")
    print(f"Part {part} answer: \033[1m{answer}\033[0m")

run_all()