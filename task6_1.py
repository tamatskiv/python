#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def ui_input() -> list:
    """This function takes sides of the triangle"""
    print('Enter three sides of the triangle:')
    sides = [int(input()), int(input()), int(input())]
    return sides

def square_triangle(sides: list) -> float:
    """This function calculates square of the triangle"""
    h_per = (sides[0] + sides[1] + sides[2]) / 2 #half-perimetr
    square = math.sqrt (h_per * (h_per- sides[0]) * (h_per - sides[1]) * (h_per - sides[2]))
    return square

def ui_output(square: float) -> None:
    """This function print square of the triangle"""
    print('Square of the triangle: %1.3f' % square)

sides = ui_input()
square = square_triangle(sides) 
ui_output(square)
