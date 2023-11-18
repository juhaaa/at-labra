import math
import heapq

class JPS:
    def __init__(self, grid, start, finish):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.sqrt2 = math.sqrt(2)
        self.dist = [[float("inf") for _ in range(self.cols)] for _ in range(self.rows)]
        self.parent = [[None for _ in range(self.cols)] for _ in range(self.rows)]
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.start_node = start[1], start[0]
        self.finish_node = finish[1], finish[0]
        self.dist[self.start_node[0]][self.start_node[1]] = 0
        self.queue = [(0, self.start_node)]
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    def heuristic(self):
        pass

    def jump(self):
        pass

    def successors(self):
        pass

    def run(self):
        pass

    def sort_data(self):
        pass