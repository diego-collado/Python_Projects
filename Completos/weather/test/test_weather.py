# Archivo test_weather.py

# IMPORTS ------------------------------------------------------
import unittest
from src.weather import get_weather

# CLASS --------------------------------------------------------
class WeatherTests(unittest.TestCase):

    def test_ciudad_invalida(self):
        resultado = get_weather("CiudadQueNoExiste123")
        self.assertIn("error", resultado)

    def test_api_key_faltante(self):
        import os
        original_key = os.environ.get("API_KEY")
        os.environ["API_KEY"] = ""
        resultado = get_weather("Madrid")
        self.assertEqual(resultado["error"], "API_KEY no configurada.")
        os.environ["API_KEY"] = original_key if original_key else ""

# MAIN --------------------------------------------------------
if __name__ == "__main__":
    unittest.main()