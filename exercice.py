#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math


def main() -> None:
    print(f"Moyenne des nombres 2.1, 4.3, 6.5: {average(2.1, 4.3, 6.5)}")

    print(
        f"Conversion de 180 degres, 2 minutes et 45 secondes en radians: {to_radians(180, 2, 45)}")

    degrees, minutes, seconds = to_degrees(2.5)
    print(
        f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


def average(a: float, b: float, c: float) -> float:
    return (a + b + c) / 3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    degres = angle_degs + angle_mins / 60 + angle_secs / 3600
    return math.radians(degres)


def to_degrees(angle_rads: float) -> tuple:
    degresBrut = math.degrees(angle_rads)
    degresNoComma = int(degresBrut)
    nombreApresVirgule = degresBrut - degresNoComma
    minutes = nombreApresVirgule * 60
    secondes = (minutes - int(minutes)) * 60
    return degresNoComma, int(minutes), int(secondes)


def to_celsius(temperature: float) -> float:
    return (temperature - 32) / 1.8


def to_farenheit(temperature: float) -> float:
    return (temperature * 1.8) + 32


if __name__ == '__main__':
    main()
