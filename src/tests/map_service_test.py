import unittest
from PIL import Image
from map_service import binary_map_to_matrix

class TestMapService(unittest.TestCase):
    def setUp(self):
        # 10x10px kuva jossa mustaa kuten identiteettimatriissa
        #[[1,0,0,0,0,0,0,0,0,0],
        #[0,1,0,0,0,0,0,0,0,0],
        #[0,0,1,0,0,0,0,0,0,0]
        #[0,0,0,1,0,0,0,0,0,0]
        #[0,0,0,0,1,0,0,0,0,0]
        #[0,0,0,0,0,1,0,0,0,0]
        #[0,0,0,0,0,0,1,0,0,0]
        #[0,0,0,0,0,0,0,1,0,0]
        #[0,0,0,0,0,0,0,0,1,0]
        #[0,0,0,0,0,0,0,0,0,1]]
        self.png_image = Image.open("src/tests/test_img/diag.png")
        self.result = binary_map_to_matrix(self.png_image)
        self.amount = 0

        
    def test_converting_image_rows_cols(self):
        # Testataan löytyykö 10 riviä
        self.assertEqual(10, len(self.result))
        # Testataan löytyykö kymmenen saraketta
        self.assertEqual(10, len(self.result[0]))

    def test_ones_in_right_places(self):
        # Testataan diagonaaliykköset
        for i in range(10):
            self.assertEqual(1, self.result[i][i])

    def test_amount_of_ones(self):
        # Testataan ykkösten määrä (10)
        for i in range(10):
            self.amount += self.result[i].count(1)
        self.assertEqual(10, self.amount)

    def test_amout_of_zeroes(self):
        # Testataan nollien määrä (90)
        for i in range(10):
            self.amount += self.result[i].count(0)
        self.assertEqual(90, self.amount)
