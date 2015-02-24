def mc_problem(start = (3, 3, 1, 0, 0, 0), goal = None):
    """Solve the missionaries and cannibals problem.  State is 6 ints: (M1, C1,
    B1, M2, C2, B2) on the start (1) and other (2) sides.  Find a path that goes
    from the initial state to the goal state (which, if not specified, is the
    state with no people or boats on the start side.) """
    if goal is None:
        goal = (0, 0, 0) + start[:3]
    if start == goal:
        return [start]
    explored = set() # set of states we have visited
    frontier = [ [start] ] # ordered list of paths we have blazed
    while frontier:
        path = frontier.pop(0)
        s = path[-1]
        for (state, action) in csuccessors(s).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    frontier.append(path2)

def csuccessors(state):
    # Norvig's solution, with a check to make sure no state has negative numbers.
    """Find successors (including those that result in dining) to this
    state. But a state where the cannibals can dine has no successors."""
    M1, C1, B1, M2, C2, B2 = state
    ## Check for state with no successor
    if C1 > M1 > 0 or C2 > M2 > 0:
        return {}
    items = []
    if B1 > 0:
        for delta, a in deltas.items():
            x = sub(state, delta)
            if all(val >= 0 for val in x):
                items.append((sub(state, delta), a + '->'))
    if B2 > 0:
        for delta, a in deltas.items():
            x = add(state, delta)
            if all(val >= 0 for val in x):
                items.append((add(state, delta), '<-' + a))
    return dict(items)

deltas = {
    (2, 0, 1,   -2,  0, -1): 'MM',
    (0, 2, 1,    0, -2, -1): 'CC',
    (1, 1, 1,   -1, -1, -1): 'MC',
    (1, 0, 1,   -1,  0, -1): 'M',
    (0, 1, 1,    0, -1, -1): 'C'}

def add(X, Y):
    "add two vectors, X and Y."
    return tuple(x+y for x, y in zip(X, Y))

def sub(X, Y):
    "subtract two vectors, X and Y."
    return tuple(x-y for x, y in zip(X, Y))
