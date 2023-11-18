import unittest
from PIL import Image
from map_service import binary_map_to_matrix
from algo_service import start_route_search

class TestAlgoService(unittest.TestCase):
    def setUp(self):
        # Avataan kuva ja muutetaan se binäärimatriisiksi jotta ohjelmia voidaan kutsua
        self.png_image = Image.open("src/tests/test_img/horiz.png")
        self.grid = binary_map_to_matrix(self.png_image)
        self.start = (0, 9)
        self.finish = (1, 8)

    def test_dijkstra_start_and_values(self):
        # Testataan haun suoritus ja arvojen palautus
        res1, res2, res3 = start_route_search(1, self.start, self.finish, self.grid)
        self.assertEqual(float, type(res1))
        self.assertEqual(list, type(res2))
        self.assertEqual(tuple, type(res2[0]))
        self.assertEqual(list, type(res3))
        self.assertEqual(list, type(res3[0]))
        self.assertEqual(bool, type(res3[0][0]))

    def test_a_star_start_and_values(self):
        # Testataan haun suoritus ja arvojen palautus
        res1, res2, res3 = start_route_search(2, self.start, self.finish, self.grid)
        self.assertEqual(float, type(res1))
        self.assertEqual(list, type(res2))
        self.assertEqual(tuple, type(res2[0]))
        self.assertEqual(list, type(res3))
        self.assertEqual(list, type(res3[0]))
        self.assertEqual(bool, type(res3[0][0]))