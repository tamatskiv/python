#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def ui_input() -> str:
    """This function takes user string"""
    string = input('Your string: ')
    return string

def is_shortest(string: str) -> int:
    """This function finds the shortest word and calculates number of letter in it"""
    first, *rest = re.sub("[^\w]", " ", string).split()
    size = len(first)
    for word in rest:
        if len(word) < size:
            size = len(word)
    return size

def ui_output(string: str) -> None:
    """This function prints the result"""
    print(string)

ui_output(is_shortest(ui_input()))