import heapq
import math

class Dijkstra:
    def __init__(self, grid, start, finish):
        """Konstruktori muodostaa tarvittavat tietorakenteet algoritmin
        suorittamista ja datan keräämistä varten varten.
        - dist: etäisyysmatriisi
        - parent: solmun edellinen solmu lyhimmällä polulla
        - visited: vieraillut solmut matriisina
        - start_node ja finish_node x ja y käännetään toimimaan sisäkkäisten listojen kanssa
        - queue: prioriteettijono
        - directions: mahdolliset suunnat (8)
        - sqrt2: diagonaalisen liikkeen kustannus 

        Args:
            grid (List): Binäärinen matriisi, "kartta"
            start (Tuple): (int x, int y)
            finish (Tuple): (intx, int y)
        """
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

    def run(self):
        """Dijkstran algoritmin suoritus

        Returns:
            Tuple: (Polun pituus, Polku, vierailulista)
        """
        while self.queue:
            current_distance, current_node = heapq.heappop(self.queue)
            if self.visited[current_node[0]][current_node[1]]:
                continue
            self.visited[current_node[0]][current_node[1]] = True
            x, y = current_node
            if current_node == self.finish_node:
                break

            for dir_row, dir_col in self.directions:
                new_row, new_col = x + dir_row, y + dir_col
                neighbor = new_row, new_col
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] == 0:
                    distance_to_neighbor = current_distance + (1 if dir_row == 0 or dir_col == 0 else self.sqrt2)

                    if distance_to_neighbor < self.dist[new_row][new_col]:
                        self.dist[new_row][new_col] = distance_to_neighbor
                        self.parent[new_row][new_col] = (x, y)
                        heapq.heappush(self.queue, (distance_to_neighbor, neighbor))
        return self.sort_data()

    def sort_data(self):
        """Metodi jäljittää reitin ja kääntää koordinaatit toimimaan kuvan kanssa.

        Returns:
            Tuple: (Polun pituus, Polku, vierailulista)
        """
        path = []
        current = self.finish_node
        while current is not None:
            path.append(current)
            current = self.parent[current[0]][current[1]]
        path_xy = [(col, row) for row, col in path]
        return self.dist[self.finish_node[0]][self.finish_node[1]], path_xy, self.visited
