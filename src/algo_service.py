from dijkstra import Dijkstra
from a_star import AStar

def start_route_search(algo, start, finish, grid):
    """Funktio valitun algoritmin suorittamiseen

    Args:
        algo (int): 1 = dijkstra, 2 = A*, 3=JPS
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
    if algo == 2:
        a_star = AStar(grid, start, finish)
        result, path, visited = a_star.run()
        print(result)
        return result, path, visited

