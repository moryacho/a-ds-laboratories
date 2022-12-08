adjacency_list = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4, 6],
}

n = len(adjacency_list)
visited = [False] * n
start = 1
path = []


def hamilton(v):
    path.append(v)
    if len(path) == n:
        if path[0] in adjacency_list[path[-1]]:
            return True
        else:
            path.pop()
            return False
    visited[v - 1] = True
    for next_v in adjacency_list[v]:
        if not visited[next_v - 1]:
            if hamilton(next_v):
                return True
    visited[v - 1] = False
    path.pop()
    return False


if hamilton(start):
    print(*path)
else:
    print("Гамильтонов цикл не найден")
