
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]




maze_map = {}
maze_map_cells = maze_map.keys()

width = len(maze[0])
height = len(maze)

for i in range(height):
    for j in range(width):
        if maze[i][j] == 0:
            maze_map[(i, j)] = {'E': 0, 'S': 0, 'N':0, 'W':0}
            if (0 <= j + 1 < width) and maze[i][j + 1] == 0:
                maze_map[(i, j)]['E'] = 1
            if (0 <= i + 1 < height) and maze[i + 1][j] == 0:
                maze_map[(i, j)]['S'] = 1
            if (0 <= i - 1 < height) and maze[i - 1][j] == 0:
                maze_map[(i, j)]['N'] = 1
            if (0 <= j - 1 < width) and maze[i][j - 1] == 0:
                maze_map[(i, j)]['W'] = 1


def start_maze(maze):
    first_col = [maze[i][0] for i in range(height)]
    return first_col.index(0)


def end_maze(maze):
    last_col = [maze[i][-1] for i in range(height)]
    return last_col.index(0)

def dfs(maze):
    start = (start_maze(maze), 0)
    dfs_path = {}
    explored = [start]
    frontier = [start]
    while len(frontier) > 0:
        curr = frontier.pop()
        for d in 'ESNW':
            if maze_map[curr][d] == True:
                if d == 'E':
                    child = (curr[0], curr[1] + 1)
                elif d == 'S':
                    child = (curr[0] + 1, curr[1])
                elif d == 'N':
                    child = (curr[0] - 1, curr[1])
                elif d == 'W':
                    child = (curr[0], curr[1] - 1)
                if child in explored:
                    continue
                explored.append(child)
                frontier.append(child)
                dfs_path[child] = curr

    fwd_path = {}
    cell = (end_maze(maze), width - 1)
    while cell != start:
        fwd_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]

    fwd_path = set(list(fwd_path.keys()) + list(fwd_path.values()))

    for i in range(height):
        for j in range(width):
            maze[i][j] = '   '

    for cell in maze_map_cells:
        cell = list(cell)
        maze[cell[0]][cell[1]] = '\033[47m   \033[0m'

    for cell in fwd_path:
        cell = list(cell)
        maze[cell[0]][cell[1]] = '\033[44m   \033[0m'

    m = [''.join(i) for i in maze]
    for i in m:
        print(i)

dfs(maze)
