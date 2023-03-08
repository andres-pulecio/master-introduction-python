
# Unit Test Code:
import unittest

class TestFruitPrices(unittest.TestCase):
    def setUp(self):
        self.precios_frutas = {"manzana": 0.5, "pera": 0.4, "platano": 0.6, "naranja": 0.3}

    def test_correct_price(self):
        cantidad = 2
        fruta = 'manzana'

        precio_total = cantidad * self.precios_frutas[fruta]

        self.assertEqual(precio_total, 1)

    def test_incorrect_price(self):
        cantidad = 2
        fruta = 'kiwi'

        with self.assertRaises(KeyError):
            precio_total = cantidad * self.precios_frutas[fruta]


if __name__ == '__main__': 
    unittest.main()