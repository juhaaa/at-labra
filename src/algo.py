from collections import deque
import math

def dijkstra(grid, start, finish):
    rows = len(grid)
    cols = len(grid[0])
    sqrt2 = math.sqrt(2)
    dist = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    parent = [[None for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    start_node = start[1], start[0]
    finish_node = finish[1], finish[0]
    dist[start_node[0]][start_node[1]] = 0
    queue = deque([(0, start_node)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        current_distance, current_node = queue.popleft()
        if visited[current_node[0]][current_node[1]]:
            continue
        visited[current_node[0]][current_node[1]] = True
        x, y = current_node
        if current_node == finish_node:
            break

        for dir_row, dir_col in directions:
            new_row, new_col = x + dir_row, y + dir_col
            neighbor = new_row, new_col
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0:
                distance_to_neighbor = current_distance + (1 if dir_row == 0 or dir_col == 0 else sqrt2)

                if distance_to_neighbor < dist[new_row][new_col]:
                    dist[new_row][new_col] = distance_to_neighbor
                    parent[new_row][new_col] = (x, y)
                    queue.append((distance_to_neighbor, neighbor))


    path = []
    current = finish_node
    while current is not None:
        path.append(current)
        current = parent[current[0]][current[1]]

    return dist[finish_node[0]][finish_node[1]], path, visited

