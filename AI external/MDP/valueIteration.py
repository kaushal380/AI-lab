REWARD = -0.01
DISCOUNT = 0.99
MAX_ERROR = 10**(-3)
NUM_ACTIONS = 4
ACTIONS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
NUM_ROW = 3
NUM_COL = 4
U = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]

def printEnvironment(arr, policy=False):
    res = ""
    for r in range(NUM_ROW):
        res += "|"
        for c in range(NUM_COL):
            if r == c == 1:
                val = "WALL"
            elif r <= 1 and c == 3:
                val = "+1" if r == 0 else "-1"
            else:
                if policy:
                    val = ["Down", "Left", "Up", "Right"][arr[r][c]]
                else:
                    val = f"{arr[r][c]:.2f}"
            res += f" {val[:5].ljust(5)} |"
        res += "\n"
    print(res)

def getU(U, r, c, action):
    dr, dc = ACTIONS[action]
    newR, newC = r + dr, c + dc
    if newR < 0 or newC < 0 or newR >= NUM_ROW or newC >= NUM_COL or (newR == 1 and newC == 1):
        return U[r][c]
    else:
        return U[newR][newC]

def calculateU(U, r, c, action):
    u = REWARD
    u += 0.1 * DISCOUNT * getU(U, r, c, (action - 1) % 4)
    u += 0.8 * DISCOUNT * getU(U, r, c, action)
    u += 0.1 * DISCOUNT * getU(U, r, c, (action + 1) % 4)
    return u

def valueIteration(U):
    print("During the value iteration:\n")
    while True:
        nextU = [[0, 0, 0, 1], [0, 0, 0, -1], [0, 0, 0, 0]]
        error = 0
        for r in range(NUM_ROW):
            for c in range(NUM_COL):
                if (r <= 1 and c == 3) or (r == 1 and c == 1):
                    continue
                nextU[r][c] = max([calculateU(U, r, c, action) for action in range(NUM_ACTIONS)])
                error = max(error, abs(nextU[r][c] - U[r][c]))
        U = nextU
        printEnvironment(U)
        if error < MAX_ERROR * (1 - DISCOUNT) / DISCOUNT:
            break
    return U

def getOptimalPolicy(U):
    policy = [[-1, -1, -1, -1] for _ in range(NUM_ROW)]
    for r in range(NUM_ROW):
        for c in range(NUM_COL):
            if (r <= 1 and c == 3) or (r == 1 and c == 1):
                continue
            maxAction, maxU = None, -float("inf")
            for action in range(NUM_ACTIONS):
                u = calculateU(U, r, c, action)
                if u > maxU:
                    maxAction, maxU = action, u
            policy[r][c] = maxAction
    return policy

print("The initial U is:\n")
printEnvironment(U)
U = valueIteration(U)
policy = getOptimalPolicy(U)
print("The optimal policy is:\n")
printEnvironment(policy, True)