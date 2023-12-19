from typing import List

def run_workflow(workflows, workflow, env):
    (name, conds) = workflow

    if not all(env.values()):
        return 0

    if name == 'R':
        return 0
    elif name == 'A':
        prod = 1
        for (lower, upper) in env.values():
            prod *= upper - lower
        return prod

    sm = 0

    for cond in conds:
        if cond[0] == 0:
            (_, var, num, target) = cond

            # split env into two parts:
            # var < num, var >= num
            lt_env = env.copy()
            gte_env = env
            
            (lower, upper) = env[var]

            lt_env[var] = ()
            gte_env[var] = ()

            lt_inv = (lower, min(upper, num))
            gte_inv = (max(lower, num), upper)

            if lt_inv[0] < lt_inv[1]:
                lt_env[var] = lt_inv
            if gte_inv[0] < gte_inv[1]:
                gte_env[var] = gte_inv

            # Run the less than condition
            sm += run_workflow(workflows, workflows[target], lt_env)

            # Go to next iteration, where env = gte_env.
            
        elif cond[0] == 1:
            (_, var, num, target) = cond

            # split env into two parts:
            # var <= num, var > num
            lte_env = env
            gt_env = env.copy()
            
            (lower, upper) = env[var]

            lte_env[var] = ()
            gt_env[var] = ()

            lte_inv = (lower, min(upper, num) + 1)
            gt_inv = (max(lower, num) + 1, upper)

            if lte_inv[0] < lte_inv[1]:
                lte_env[var] = lte_inv
            if gt_inv[0] < gt_inv[1]:
                gt_env[var] = gt_inv
            
            # Run the greater than condition
            sm += run_workflow(workflows, workflows[target], gt_env)
        elif cond[0] == 2:
            # Run the fallback workflow 
            sm += run_workflow(workflows, workflows[cond[1]], env)

    return sm
    

def solve(inp: List[str]):
    workflows = {}

    workflows['R'] = ('R', ())
    workflows['A'] = ('A', ())

    i = 0
    for ln in inp:
        if not ln.strip():
            break
        spl = ln.split('{')
        name = spl[0]

        conds = spl[1][:-1].split(",")

        newconds = []
        for c in conds:
            if '<' in c:
                c = c.split('<')
                var = c[0]
                right = c[1].split(":")
                num = int(right[0])
                ins = right[1]
                # type, var, num, target
                newconds.append((0, var, num, ins))
            elif '>' in c:
                c = c.split('>')
                var = c[0]
                right = c[1].split(":")
                num = int(right[0])
                ins = right[1]
                # type, var, num, target
                newconds.append((1, var, num, ins))
            else:
                newconds.append((2, c))

        workflows[name] = (name, newconds)

        i += 1
    
    env = {}
    env["x"] = (1, 4001)
    env["m"] = (1, 4001)
    env["a"] = (1, 4001)
    env["s"] = (1, 4001)

    return run_workflow(workflows, workflows["in"], env)