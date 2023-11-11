from algo import dijkstra

def start_route_search(algo, start, finish, grid):
    """Funktio valitun algoritmin suorittamiseen

    Args:
        algo (int): 1 = dijkstra, 2 = JPS
        start (tuple, int): Aloituskoordinaatit
        finish (tuple, int): MAalikorrdinaatit
        grid (list): matriisikartta

    Returns:
        _type_: _description_
    """
    if algo == 1:
        result, path, visited = dijkstra(grid, start, finish)
        for row in path:
            print(row)
    return result, path, visited
