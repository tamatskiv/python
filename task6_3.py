#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math

def ui_input() -> list:
    """This function takes initial deposit, final deposit and percentages""" 
    print('Enter initial deposit, final deposit and percentages: ')
    return [int(input()), int(input()), int(input())]

def calc_duration(value: list) -> float:
    """This function calculates duration of the deposit"""
    duration = math.log(value[1] / value[0], 1 + value[2]/100)
    return duration

def ui_output(duration: float) -> None:
    """This function prints duration of the deposit"""
    print('Duration: %1.2f' % duration)

ui_output(calc_duration(ui_input()))
