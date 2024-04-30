import unittest

def contar_vocales(palabra):

    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    for letra in palabra:
        if letra in vocales:
            if letra in resultado.keys():
                resultado[letra] += 1
            else:
                resultado[letra] = 1

    return resultado

class TestContarVocales(unittest.TestCase):
    def test_nada(self):
        palabra = "zzzz"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {})
    
    def test_con_vocal_o(self):
        palabra = "sol"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 1})
    
    def test_con_vocal_doble_o(self):
        palabra = "solo"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"o": 2})
    
    def test_con_todas_las_vocales(self):
        palabra = "murcielago"
        resultado = contar_vocales(palabra)
        self.assertEqual(resultado, {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1},)
    
    def test_con_vocales_en_mayuscula(self):
        palabra = "SOlAmente quIerO"
        resultado = contar_vocales(palabra.lower())
        self.assertEqual(resultado, {"a": 1, "e": 3, "i": 1, "o": 2, "u": 1},)


unittest.main()