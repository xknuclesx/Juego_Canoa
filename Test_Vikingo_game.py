import unittest
from Vikingo_game import es_estado_valido, cruzar_rio

class TestVikingoGame(unittest.TestCase):

    def test_es_estado_valido(self):
        self.assertTrue(es_estado_valido(["vikingo", "lobo", "caperucita", "uvas"])[0])
        self.assertFalse(es_estado_valido(["lobo", "caperucita", "uvas"])[0])
        self.assertEqual(es_estado_valido(["lobo", "caperucita", "uvas"])[1], "💀El lobo se comió a la caperucita💀")
        self.assertFalse(es_estado_valido(["caperucita", "uvas"])[0])
        self.assertEqual(es_estado_valido(["caperucita", "uvas"])[1], "🍴La caperucita se comió las uvas🍴")

    def test_cruzar_rio_derecha(self):
        orilla_izquierda = ["vikingo", "lobo", "caperucita", "uvas"]
        orilla_derecha = []
        nueva_orilla_izquierda, nueva_orilla_derecha, mensaje = cruzar_rio(orilla_izquierda, orilla_derecha, "lobo", "derecha")
        self.assertEqual(nueva_orilla_izquierda, ["caperucita", "uvas"])
        self.assertEqual(nueva_orilla_derecha, ["vikingo", "lobo"])
        self.assertEqual(mensaje, "")

    def test_cruzar_rio_izquierda(self):
        orilla_izquierda = ["caperucita", "uvas"]
        orilla_derecha = ["vikingo", "lobo"]
        nueva_orilla_izquierda, nueva_orilla_derecha, mensaje = cruzar_rio(orilla_izquierda, orilla_derecha, "lobo", "izquierda")
        self.assertEqual(nueva_orilla_izquierda, ["caperucita", "uvas", "vikingo", "lobo"])
        self.assertEqual(nueva_orilla_derecha, [])
        self.assertEqual(mensaje, "")

    def test_cruzar_rio_objeto_no_en_orilla(self):
        orilla_izquierda = ["vikingo", "caperucita", "uvas"]
        orilla_derecha = ["lobo"]
        nueva_orilla_izquierda, nueva_orilla_derecha, mensaje = cruzar_rio(orilla_izquierda, orilla_derecha, "lobo", "derecha")
        self.assertIsNone(nueva_orilla_izquierda)
        self.assertIsNone(nueva_orilla_derecha)
        self.assertEqual(mensaje, "El objeto lobo no está en la orilla izquierda.")

    def test_estado_no_valido_despues_de_cruzar(self):
        orilla_izquierda = ["vikingo", "lobo", "uvas"]
        orilla_derecha = ["caperucita"]
        nueva_orilla_izquierda, nueva_orilla_derecha, mensaje = cruzar_rio(orilla_izquierda, orilla_derecha, "lobo", "derecha")
        self.assertIsNone(nueva_orilla_izquierda)
        self.assertIsNone(nueva_orilla_derecha)
        self.assertEqual(mensaje, "🍴La caperucita se comió las uvas🍴")

if __name__ == "__main__":
    unittest.main()
