from typing import List

def run_workflow(workflows, workflow, env):
    (name, conds) = workflow

    if name == 'R':
        return False
    elif name == 'A':
        return True

    for cond in conds:
        if cond[0] == 0:
            (_, var, num, target) = cond
            if var in env and env[var] < num:
                return run_workflow(workflows, workflows[target], env)
        elif cond[0] == 1:
            (_, var, num, target) = cond
            if var in env and env[var] > num:
                return run_workflow(workflows, workflows[target], env)
        elif cond[0] == 2:
            return run_workflow(workflows, workflows[cond[1]], env)
    

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
    
    sm = 0
    for ln in inp[i+1:]:
        ln = ln[1:-1]
        ln = ln.split(",")

        env = {}
        for spl in ln:
            spl = spl.split("=")
            env[spl[0]] = int(spl[1])
        
        if run_workflow(workflows, workflows["in"], env):
            sm += sum(env.values())
    return sm