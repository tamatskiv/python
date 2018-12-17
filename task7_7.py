#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

def ui_input() -> str:
    """This function takes user string"""
    string = input('Your string: ')
    return string

def to_snake_case(string: str) -> str:
    """This function changes writing to Snake Case"""
    result = re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()
    return result

def to_camel_case(string: str) -> str:
    """This function changes writing to Camel Case"""
    first, *rest = string.split('_')
    result = first + ''.join(word.capitalize() for word in rest)
    return result

def ui_output(string: str) -> None:
    """This function print the result"""
    print(string)

ui_output(to_camel_case(to_snake_case(ui_input())))


