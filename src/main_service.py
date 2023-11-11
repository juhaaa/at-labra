from algo import dijkstra
def start_route_search(algo, start, finish, grid):
    if algo == 1:
        result, path, visited = dijkstra(grid, start, finish)
        for row in path:
            print(row)
    return result, path, visited
