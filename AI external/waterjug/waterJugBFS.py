from collections import deque

def bfs(a, b, target):
    visited = set()
    path = []
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        if (x, y) in visited or x > a or y > b or x < 0 or y < 0:
            continue

        path.append((x, y))
        visited.add((x, y))

        if x == target or y == target:
            path.append((x, 0) if x == target else (0, y))
            for p in path:
                print(p)
            return

        queue.extend([(x, b), (a, y), (0, y), (x, 0)])

        for ap in range(max(a, b) + 1):
            queue.extend([(x + ap, y - ap) if x + ap <= a and y - ap >= 0 else (x - ap, y + ap)])

    print("No solution")

if __name__ == '__main__':
    bfs(4, 3, 2)