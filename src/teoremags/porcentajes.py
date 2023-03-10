"""Funciones de porcentajes."""


def error_porcentual(
        valor_real: float | int,
        valor_aprox: float | int
        ) -> float:
    """Calcula el porcentaje de error."""

    return (abs(valor_aprox - valor_real) / valor_real) * 100
