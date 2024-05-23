from collections import defaultdict

a, b, target = 4, 3, 2
visited = defaultdict(lambda: False)
def waterJugSolver(x, y):
    if (x == target and y == 0) or (y == target and x == 0):
        print(x, y)
        return True
    if not visited[(x, y)]:
        print(x, y)
        visited[(x, y)] = True
        return (waterJugSolver(0, y) or waterJugSolver(x, 0) or
                waterJugSolver(a, y) or waterJugSolver(x, b) or
                waterJugSolver(x + min(y, a - x), y - min(y, a - x)) or
                waterJugSolver(x - min(x, b - y), y + min(x, b - y)))
    return False

print("Steps: ")
waterJugSolver(3, 0)