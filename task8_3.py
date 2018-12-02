#!/usr/bin/env python3
# -*- coding: utf-8 -*-

numbers = [2, 5, 5, 7, 12, 13, 13]

def calc_average(numbers: list) -> float:
    """This function calculates average value of the list"""
    return sum(numbers) / len(numbers)

def calc_median(numbers: list) -> float:
    """This function calculates median of the list"""
    length = len(numbers)
    numbers = sorted(numbers)
    if length % 2 == 1:
        return numbers[length//2]
    else: 
        return (numbers[length//2 - 1] + numbers[length//2]) / 2

def ui_output(average: float, median: float) -> None:
    """This function prints list, average value and median of the list"""
    print('List: ', numbers, '\nAverage value:', average, '\nMedian: ', median)

ui_output(calc_average(numbers), calc_median(numbers))

