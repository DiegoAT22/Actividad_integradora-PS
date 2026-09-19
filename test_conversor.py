import pytest

from conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    kilometros_a_millas,
    millas_a_kilometros,
    pesos_a_dolares,
    dolares_a_pesos
)


@pytest.mark.unit
def test_celsius_a_fahrenheit():
    resultado = celsius_a_fahrenheit(25)
    assert resultado == 77


@pytest.mark.unit
def test_kilometros_a_millas():
    resultado = kilometros_a_millas(10)
    assert round(resultado, 2) == 6.21


@pytest.mark.unit
def test_pesos_a_dolares():
    resultado = pesos_a_dolares(185)
    assert resultado == 10


@pytest.mark.parametrize(
    "celsius, esperado",
    [
        (0, 32),
        (25, 77),
        (100, 212)
    ]
)
def test_varias_temperaturas(celsius, esperado):
    assert celsius_a_fahrenheit(celsius) == esperado