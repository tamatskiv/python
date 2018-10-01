#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def ui_input() -> list:
    """This function takes """
    print('Enter initial deposit, percentages, duration of the deposit: ')
    parameters = [int(input()), int(input()), int(input())]
    return parameters

def calc_deposit(parameters: list) -> float:
    deposit = parameters[0] * (1 + (parameters[1]/100))**parameters[2]
    return deposit

def ui_output(deposit: float) -> None:
    print('Your money at the end of duration of the deposit: %1.3f ' % deposit)

parameters = ui_input()
deposit = calc_deposit(parameters)
ui_output(deposit)
