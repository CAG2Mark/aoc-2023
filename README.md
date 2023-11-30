# aoc-2023
Advent of Code 2023 solutions

# Running
This year, I've made a runner in `aoc.py` that automatically downloads inputs and sets up a simple skeleton:
```
usage: aoc-run [-h] [-f] [-n] [-p PART] [-e] day

positional arguments:
  day                   Which day to run. (Required)

options:
  -h, --help            show this help message and exit
  -f, --force-input     Force downloads the input.
  -n, --no-run          Do not run the solutions.
  -p PART, --part PART  Only run a certain part.
  -e, --use-example     Uses the example input stored in day<day>/ex.
```
Simply place your session cookie in a file `session` and you should be good to go.
