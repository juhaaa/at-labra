from dijkstra import Dijkstra

def start_route_search(algo, start, finish, grid):
    """Funktio valitun algoritmin suorittamiseen

    Args:
        algo (int): 1 = dijkstra, 2 = JPS
        start (tuple, int): Aloituskoordinaatit
        finish (tuple, int): MAalikorrdinaatit
        grid (list): matriisikartta

    Returns:
        Float: result
        List: path, lista tupleja
        List: visited, matriisi vierailluista solmuista
    """
    if algo == 1:
        dijkstra = Dijkstra(grid, start, finish)
        result, path, visited = dijkstra.run()
        print(result)
    return result, path, visited
