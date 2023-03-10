def test_angulos():
    """Comprueba el correcto funcionamiento de la clase Angulo."""

    from src.teoremags.definiciones import Angulo
    print(Angulo.desde_grados_decimales(25.667).a_radianes())
    print("25.667 == 0.44797...")


if __name__ == "__main__":
    print(" ****** TEST FUNCIONAL ******")
