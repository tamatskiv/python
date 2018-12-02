#!/usr/bin/env python3
# -*- coding:utf-8 -*-

def ui_input() -> list:
    """This function takes initial deposit, percentages and duration""" 
    print('Enter initial deposit, percentages and duration: ')
    return [int(input()), int(input()), int(input())]

def calc_deposit(value: list) -> float:
    """This function calculates final deposit"""
    deposit = value[0] * (1 + (value[1])/100)* value[2]
    return deposit

def ui_output(deposit: float) -> None:
    """This function prints final deposit"""
    print('Your deposit: %1.2f' % deposit)

ui_output(calc_deposit(ui_input()))
