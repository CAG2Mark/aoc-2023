#!/usr/bin/python3

import argparse
import os
import requests

YEAR = 2023

parser = argparse.ArgumentParser(
                    prog='aoc-run')

parser.add_argument('day', help="which day to run (required)")
parser.add_argument('-f', '--force-input', action='store_true', help="force downloads the input") # Force fetch input
parser.add_argument('-s', '--setup-only', action='store_true', help="just set up the folder for the day then exit") # Force fetch input
parser.add_argument('-n', '--no-run', action='store_true', help="do not run the solutions") # Do not run
parser.add_argument('-p', '--part', help="only run a certain part") # Part. If none provided then both are run
parser.add_argument('-e', '--use-example', action='store_true', help="uses the example input stored in day<day>/ex") # Use "ex" file instead

args = parser.parse_args()

day = args.day
force_input = args.force_input
part = args.part
setup_only = args.setup_only
norun = args.no_run
use_example = args.use_example

session = open("session", "r").read().strip()
cookies = {"session": session}

daypath = f"day{str(day).rjust(2, '0')}"

def create_template():
    if not os.path.exists(daypath):
        os.mkdir(f"{daypath}")

    template = open("TEMPLATE.py", "r").read()

    def write_if_none(path: str, contents: str):
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(contents)

    write_if_none(f"{daypath}/p1.py", template)
    write_if_none(f"{daypath}/p2.py", template)
    write_if_none(f"{daypath}/ex", "")

create_template()

if setup_only:
    print(f"Set up the folder for day {day}.")
    exit(0)

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