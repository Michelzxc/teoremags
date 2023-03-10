"""Define objetos matemáticos simples con propiedades."""

from .constantes import Constantes as Const


class Angulo(Const):
    def __init__(self):
        self.modulo = 0.0
        self.tipo = None

    def __str__(self):
        return f"Angulo({self.modulo}, {self.tipo})"

    @staticmethod
    def desde_radianes(modulo: float | int) -> "Angulo":
        """Crea un objeto Angulo desde radianes."""

        angulo = Angulo()
        if type(modulo) not in (float, int):
            raise TypeError(f"{type(modulo)}")
        angulo.modulo = modulo
        angulo.tipo = "rad"
        return angulo

    @staticmethod
    def desde_grados_decimales(modulo: float | int) -> "Angulo":
        """Crea un objeto Angulo desde grados sexagesimales tipo decimal.

        No confundir con gradianes (gra)!, son grados sexagesimales (deg).
        """

        angulo = Angulo()
        angulo.modulo = modulo
        angulo.tipo = "deg"
        return angulo

    @staticmethod
    def desde_grados_sexagesimales(modulo: list) -> "Angulo":
        """Convierte grados sexagesimales a grados decimales.

        'modulo' puede ser:
            - una lista: [h, m, s] con 'h' y 'm' int y 's' int o float.

        Retorna un objeto Angulo con tipo Grado (en decimales).
        """

        deg10 = modulo[0]
        div = 60
        for g in modulo[1:]:
            deg10 += g / div
            div *= 60

        return Angulo.desde_grados_decimales(deg10)

    def mostrar(self) -> tuple:
        """Retorna el valor del ángulo y el tipo."""

        return self.modulo, self.tipo

    @staticmethod
    def deg2rad(valor: float) -> float:
        """Convierte Grados sexagesimales tipo decimal a radianes."""

        return valor * (Const.pi / 180)

    @staticmethod
    def rad2deg(valor: float) -> float:
        """Convierte radianes a grados sexagesimales tipo decimal."""

        return valor * (180 / Const.pi)

    def a_radianes(self) -> float:
        """Devuelve el módulo en radianes."""

        if self.tipo == "rad":
            return self.modulo
        elif self.tipo == "deg":
            return self.deg2rad(self.modulo)
        else:
            raise NotImplemented()

    def a_grados_decimales(self) -> float:
        """Devuelve el módulo en grados sexagesimales tipo decimal."""

        if self.tipo == "deg":
            return self.modulo
        elif self.tipo == "rad":
            return self.rad2deg(self.modulo)
        else:
            raise NotImplemented()
