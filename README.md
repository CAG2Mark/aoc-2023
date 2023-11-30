# aoc-2023
Advent of Code 2023 solutions

# Running
This year, I've made a runner in `aoc.py` that automatically downloads inputs and sets up a simple skeleton:
```
usage: aoc-run [-h] [-f] [-n] [-p PART] [-e] day

positional arguments:
  day                   which day to run (required)

options:
  -h, --help            show this help message and exit
  -f, --force-input     force downloads the input
  -n, --no-run          do not run the solutions
  -p PART, --part PART  only run a certain part
  -e, --use-example     uses the example input stored in day<day>/ex
```
Simply place your session cookie in a file `session` and you should be good to go.
