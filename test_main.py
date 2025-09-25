import unittest
from main import dar_vuelta_texto

class TestDarVueltaTexto(unittest.TestCase):
    def test_invertir_texto_simple(self):
        resultado = dar_vuelta_texto("hola")
        self.assertEqual(resultado, "aloh")

    def test_invertir_texto_vacio(self):
        resultado = dar_vuelta_texto("")
        self.assertEqual(resultado, "")

    def test_invertir_texto_con_espacios(self):
        resultado = dar_vuelta_texto("hola mundo")
        self.assertEqual(resultado, "odnum aloh")

    def test_invertir_texto_con_numeros(self):
        resultado = dar_vuelta_texto("123abc")
        self.assertEqual(resultado, "cba321")

if __name__ == "__main__":
    unittest.main()
