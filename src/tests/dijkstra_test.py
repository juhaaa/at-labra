import unittest
from PIL import Image
from map_service import binary_map_to_matrix
from dijkstra import Dijkstra
import math

class TestDijkstra(unittest.TestCase):
    def setUp(self):
        # 10x10px kuva jonka halkaisee horisontaalisesti musta "este"
        # Muodostetaan kuvasta matriisi
        #[[0,0,0,0,0,0,0,0,0,0],
        #[0,0,0,0,0,0,0,0,0,0],
        #[0,0,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,0,0,0,0]
        #[1,1,1,1,1,1,1,1,1,1]
        #[0,0,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,0,0,0,0]
        #[0,0,0,0,0,0,0,0,0,0]]
        self.png_image = Image.open("src/tests/test_img/horiz.png")
        self.grid = binary_map_to_matrix(self.png_image)

    def test_correct_distance_diagonal(self):
        # Testataan yksi diagonaalisiirtymä arvoltaan sqrt(2)
        start = (0, 9)
        finish = (1, 8)
        dijkstra_d = Dijkstra(self.grid, start, finish)
        dist = dijkstra_d.run()[0]
        self.assertEqual(dist, math.sqrt(2))
        # Alku ja loppu käännettynä
        dijkstra_d = Dijkstra(self.grid, finish, start)
        dist = dijkstra_d.run()[0]
        self.assertEqual(math.sqrt(2), dist)

    def test_correct_distance_orthogonal(self):
        # Testataan kolmen siirtymä sivuttain arvoltaan 3
        start = (0, 9)
        finish = (3, 9)
        dijkstra_o = Dijkstra(self.grid, start, finish)
        dist = dijkstra_o.run()[0]
        self.assertEqual(3, dist)
        # Käännettynä
        dijkstra_o = Dijkstra(self.grid, finish, start)
        dist = dijkstra_o.run()[0]
        self.assertEqual(3, dist)

    def test_not_found(self):
        # Testataan tilanne, jossa reittiä ei ole
        start = (0, 9)
        finish = (9, 0)
        dijkstra_inf = Dijkstra(self.grid, start, finish)
        dist = dijkstra_inf.run()[0]
        self.assertEqual(float("inf"), dist)

    def test_length_of_path(self):
        # Testataan polun pituus
        # Mukana aloitus-solmu
        start = (0, 9)
        finish = (3, 9)
        dijkstra_p = Dijkstra(self.grid, start, finish)
        path= dijkstra_p.run()[1]
        self.assertEqual(4, len(path))

    def test_correct_nodes_in_path(self):
        # Testataan oikea reitti
        start = (0, 9)
        finish = (3, 9)
        correct_nodes = [(3, 9), (2, 9), (1, 9), (0, 9)]
        dijkstra_p = Dijkstra(self.grid, start, finish)
        path= dijkstra_p.run()[1]
        for node in correct_nodes:
            self.assertIn(node, path)
