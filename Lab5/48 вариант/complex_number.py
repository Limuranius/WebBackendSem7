from enum import Enum
import cmath


class ComplexFormat(Enum):
    POLAR = "Тригонометрическая"
    EULER = "Показательная"
    REGULAR = "Обычная"


class Complex:
    real: float
    im: float

    def __init__(self, real: float, im: float):
        self.real = real
        self.im = im

    def modulus(self) -> float:
        return abs(complex(self.real, self.im))

    def to_format(self, form: ComplexFormat):
        r, phi = cmath.polar(complex(self.real, self.im))
        match form:
            case ComplexFormat.POLAR:
                fmt = "z = {r} * (cos({phi}) + i * sin({phi}))"
                return fmt.format(
                    r=r,
                    phi=phi
                )
            case ComplexFormat.EULER:
                fmt = "z = {r} * e^(i * {phi})"
                return fmt.format(
                    r=r,
                    phi=phi
                )
            case ComplexFormat.REGULAR:
                fmt = "z = {real} + {im} * i"
                return fmt.format(
                    real=self.real,
                    im=self.im
                )
            case _:
                return ""

    @classmethod
    def from_polar(cls, r: float, phi: float):
        z = cmath.rect(r, phi)
        return Complex(z.real, z.imag)
