adjacency_list = {
    1: [2, 8],
    2: [1, 3, 8],
    3: [2, 4, 8],
    4: [3, 7, 9],
    5: [6, 7],
    6: [5],
    7: [4, 5, 8],
    8: [1, 2, 3, 7],
    9: [4, 6]
}


def bfs(start, end, graph, visited):
    n = len(graph)
    queue = [start]

    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            return True

        next_vs = graph[current]
        for next_v in next_vs:
            if next_v not in visited:
                queue.append(next_v)
                visited[next_v] = current

    return False


start = int(input("Введите номер стартовой вершины: "))
end = int(input("Введите номер конечной вершины: "))
visited = {start: None}
answer = bfs(start, end, adjacency_list, visited)

if answer:
    print(f"Путь от {start} вершины до {end}")
    current = end
    print(end, end=' ')
    while current != start:
        current = visited[current]
        print(f"<- {current}", end=' ')
else:
    print("Путь не найден")
